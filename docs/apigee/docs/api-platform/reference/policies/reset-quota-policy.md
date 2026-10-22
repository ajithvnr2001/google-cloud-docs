---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reset-quota-policy/
title: ResetQuota policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:13.892022+00:00
---

# ResetQuota policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reset-quota-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  ResetQuota policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Use the ResetQuota policy to dynamically modify the remaining number of requests allowed by the target Quota policy. You typically use this policy to decrease the current quota count of the target Quota policy rather than waiting for the quota count to reset. 

For example, the target Quota policy limits a developer to 1000 requests per week. By the second day of the week, the developer has already reached this limit. Use the Reset Quota policy to subtract 500 from their quota counter to allow an additional 500 requests for the remainder of the week. At the end of the week, the Quota policy resets, and the developer is back to 1000 requests for the week.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

See [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) for more on the Quota policy. Also see [this community post](https://discuss.google.dev/t/how-to-use-reset-quota-correctly/7564.html) on using the Reset Quota policy. 

### Samples

These policy code samples illustrate how to reset quota counters:

### Reset Default Counter
    
    
    <ResetQuota name="resetQuota">
       <Quota name="MyQuotaPolicy">
          <Identifier name="_default">
             <Allow>100</Allow>
          </Identifier>
       </Quota>
    </ResetQuota>

The Reset Quota policy specifies the target Quota policy by using the name attribute of the <Quota> tag. In the example above, the MyQuotaPolicy policy is the target.

All Reset Quota policies require the <Identifier> tag to specify the counter in the Quota policy to update. By default, a Quota policy has a single counter, unless the Quota policy also includes the <Identifier> tag. In this example, the target Quota policy does not use the <Identifier> tag, so you specify the name attribute as _default.

The <Allow> element specifies the value used to decrease the current quota count on the target policy. In this example, the quota count is decreased by 100, to allow 100 more requests to the target Quota policy. When the target Quota policy resets, this change is discarded.

Shown below is the definition of the target Quota policy:
    
    
    <Quota name="MyQuotaPolicy">
      <Interval>5</Interval>
      <TimeUnit>hour</TimeUnit>
      <Allow count="100"/>
    </Quota>

### Use a Reference
    
    
    <ResetQuota name="resetQuota">
       <Quota ref="request.header.quotapolicy">
          <Identifier name="_default">
             <Allow ref="request.header.allowquota" />
          </Identifier>
       </Quota>
    </ResetQuota>

In this example, you pass the name of the target Quota policy, and the change to its quota count, as headers in the request. You can then reference the flow variables containing these values in the Reset Quota policy. 

### Specify the Identifier
    
    
    <ResetQuota name="resetQuota">
       <Quota name="QuotaPolicy">
          <Identifier ref="request.header.clientId">
             <Allow>100</Allow>
          </Identifier>
       </Quota>
    </ResetQuota>

If the target Quota policy specifies the <Identifier> tag, then you can specify the same value to the <Identifier> tag of the Reset Quota policy to update a specific quota count. Notice how the <Identifier> tag in the target Quota policy below matches the value specified to the Reset Quota policy: 
    
    
    <Quota name="QuotaPolicy">
      <Identifier ref="request.header.clientId"/>
      <Interval>5</Interval>
      <TimeUnit>hour</TimeUnit>
      <Allow count="100"/>
    </Quota>

* * *

## Element reference

The element reference describes the elements and attributes of the Reset Quota policy.
    
    
    <ResetQuota async="false" continueOnError="false" enabled="true" name="Reset-Quota-1">
       <DisplayName>Reset Quota 1</DisplayName>
       <Quota name="quotaName" ref="request.header.quotapolicy">
          <Identifier name="identifierName" ref="request.header.identifier">
             <Class ref="request.header.classIdentifier" />
             <Allow>100</Allow>
          </Identifier>
       </Quota>
    </ResetQuota>

## <ResetQuota> attributes
    
    
    <ResetQuota async="false" continueOnError="false" enabled="true" name="Reset-Quota-1">

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
  
## <Quota> element

Identifies the target Quota policy whose counter should be updated.
    
    
    <Quota name="quotaName"  ref="request.header.quotapolicy">
       <Identifier name="identifierName" ref="request.header.identifier">
          <Allow>100</Allow>
       </Identifier>
    </Quota>

**Default:** | N/A  
---|---  
**Presence:** | Required  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
name |  Specifies the name of the target Quota policy.  | N/A | Optional  
ref | A flow variable that contains the name of the target Quota policy. If both ref and name are specified, then ref gets priority. If ref does not resolve at runtime, then name is used. | N/A | Optional  
  
## <Quota>/<Identifier> element

Variable used to uniquely identify the counter if the target Quota policy specifies the <Identifier> tag. 
    
    
    <Quota name="quotaName">
       <Identifier name="identifierName" ref="request.header.identifier">
          <Allow>100</Allow>
       </Identifier>
    </Quota>

**Default:** | N/A  
---|---  
**Presence:** | Required  
**Type:** | String  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
name |  Specifies the name of the count identifier in the target Quota policy. For a Quota policy that does not use the <Identifier> tag, specify _default. | N/A | Optional  
ref |  A flow variable that contains the name of the count identifier in the target Quota policy. If both ref and name are specified, then ref gets priority. If ref does not resolve at runtime, then name is used. | N/A | Optional  
  
## <Quota>/<Identifier>/<Allow> element

Specifies the amount to decrease the quota counter. You must specify <Allow>, otherwise, the policy does not modify the quota.
    
    
    <Identifier name="identifierName" ref="request.header.identifier">
       <Allow ref="request.header.allowquota">100</Allow>
    </Identifier>

**Default:** | N/A  
---|---  
**Presence:** | Required  
**Type:** | Integer  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
ref |  A flow variable that contains the change to the quota count in the target Quota policy.  | N/A | Optional  
  
## <Quota>/<Identifier>/<Class> element

Specifies the class for which the Quota counter is updated. For more on using class with the Quota policy, see [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy). 
    
    
    <Identifier name="_default">
       <Class ref="request.header.classIdentifier">
         <Allow>200</Allow>
       </Class>
    </Identifier>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
ref |  Reference to the flow variable that contains the quota class to update. | N/A | Optional  
  
## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`policies.resetquota.InvalidRLPolicy` | `500` | The `Quota` policy specified in the `<Quota>` element of the `ResetQuota` policy is not defined in the API proxy and thus is not available during the flow. The `<Quota>` element is mandatory and identifies the target `Quota` policy whose counter should be updated through the `ResetQuota` policy. | [ _build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/reset-quota-runtime-errors#invalidrlpolicy)  
`policies.resetquota.FailedToResolveAllowCountRef` | N/A | The reference to the variable containing the allow count in the `<Allow>` element of the policy cannot be resolved to a value. This element is mandatory and specifies the amount to decrease the quota counter. | [ _build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/reset-quota-runtime-errors#failedtoresolveallowcountref)  
`policies.resetquota.FailedToResolveRLPolicy` | `500` | The variable referenced by the `ref` attribute in the `<Quota>` element cannot be resolved. | [ _build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/reset-quota-runtime-errors#failedtoresolverlpolicy)  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ next to the error's cause description to visit the troubleshooting page. Error name | Cause | Fix  
---|---|---  
`InvalidCount` |  If the count value specified in the `<Allow>` element of the `ResetQuota` Policy is not an integer, then the deployment of the API proxy fails.  | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/reset-quota-deployment-errors#invalidcount)  
  
## Schemas

**Sample:** See our [GitHub repository](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) samples for the most recent schemas.

## Related topics

[Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
