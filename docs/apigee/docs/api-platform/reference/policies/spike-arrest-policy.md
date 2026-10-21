---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy/
title: SpikeArrest policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:58:27.495793+00:00
---

# SpikeArrest policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SpikeArrest policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The SpikeArrest policy protects against traffic surges with the [`<Rate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate) element. This element throttles the number of requests processed by an API proxy and sent to a backend, protecting against performance lags and downtime.

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

#### The difference between SpikeArrest and Quota

The [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) configures the number of request messages that a client app is allowed to submit to an API over the course of an hour, day, week, or month. The Quota policy enforces consumption limits on client apps by maintaining a distributed counter that tallies incoming requests.

Use Quota to enforce business contracts or SLAs with developers and partners, rather than for operational traffic management. Use SpikeArrest to protect against sudden spikes in API traffic. See also [Comparing Quota and SpikeArrest policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/comparing-quota-and-spike-arrest-policies).

#### Videos

These videos discuss use cases for this policy:

### Why You Need It

### Compare Quota Policy

## `<SpikeArrest>` element

Defines the SpikeArrest policy.

**Default Value** | See **Default Policy** tab, below  
---|---  
**Required?** | Optional  
**Type** | Complex object  
**Parent Element** |  n/a   
**Child Elements** |  [`<Identifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#identifier)  
[`<MessageWeight>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#messageweight)  
[`<Rate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate) (Required)  
[`<UseEffectiveCount>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount)  
  
  
### Syntax

The `<SpikeArrest>` element uses the following syntax:
    
    
    <SpikeArrest
      continueOnError="[false|true]"
      enabled="[true|false]"
      name="policy_name"
    >
      <DisplayName>display_name</DisplayName>
      <Properties/>
      <Identifier ref="flow_variable"/>
      <MessageWeight ref="flow_variable"/>
      <Rate ref="flow_variable">rate[pm|ps]</Rate>
      <UseEffectiveCount>[false|true]</UseEffectiveCount>
    </SpikeArrest>

### Default Policy

The following example shows the default settings when you add a SpikeArrest policy to your flow in the UI:
    
    
    <SpikeArrest async="false" continueOnError="false" enabled="true" name="Spike-Arrest-1">
      <DisplayName>Spike Arrest-1</DisplayName>
      <Properties/>
      <Identifier ref="request.header.some-header-name"/>
      <MessageWeight ref="request.header.weight"/>
      <Rate>30ps</Rate>
      <UseEffectiveCount>false</UseEffectiveCount>
    </SpikeArrest>

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
## Examples

The following examples show some of the ways in which you can use the SpikeArrest policy:

### Example 1

The following example sets the rate to five per second:
    
    
    <SpikeArrest name="SA-Static-5ps">
      <Rate>5ps</Rate>
      <UseEffectiveCount>false</UseEffectiveCount>
    </SpikeArrest>

This sample policy allows a maximum of 5 requests per second. Via smoothing, it is enforced as a maximum of one request for every 200 _millisecond_ (1000/5) interval. 

### Example 2

The following example sets the rate to 12 per minute:
    
    
    <SpikeArrest name="SA-Static-12pm">
      <Rate>12pm</Rate>
      <UseEffectiveCount>true</UseEffectiveCount>
    </SpikeArrest>

This sample policy allows a maximum of 12 requests per minute at the rate of one request per 5 _second_ (60/12) interval. If there is more than one request in the 5 _second_ interval, such requests are allowed (no smoothing) provided the number of requests is less than the configured rate limit of 12 per minute.

### Example 3

The following example restricts requests to 12 per minute (one request allowed every five seconds, or 60/12):
    
    
    <SpikeArrest name="SA-With-Dynamic-Weight-1">
      <Rate>12pm</Rate>
      <Identifier ref="client_id" />
      <MessageWeight ref="request_specific_weight" />
      <UseEffectiveCount>true</UseEffectiveCount>
    </SpikeArrest>

In addition, the [`<MessageWeight>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#messageweight) element accepts a custom value (the `weight` header) that adjusts message weights for specific apps or clients. This provides additional control over throttling for entities that are identified with the [`<Identifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#identifier) element.

### Example 4

The following example instructs SpikeArrest to look for a runtime value set via the request that is passed in as the `request.header.runtime_rate` flow variable:
    
    
    <SpikeArrest name="SA-From-Inbound-Header-1">
      <Rate ref="request.header.runtime_rate" />
      <UseEffectiveCount>true</UseEffectiveCount>
    </SpikeArrest>

The value of the flow variable must be in the form of int`pm` or int`ps`.

To try this example, execute a request like the following:
    
    
    curl http://myorg-myenv.apigee.net/price -H 'runtime_rate:30ps'

**Tip:** Check out [ How can I use API products to set spike arrest limits?](https://www.googlecloudcommunity.com/gc/Apigee/How-can-I-use-API-products-to-set-spike-arrest-limits/td-p/60175) that explains how to set the SpikeArrest rate using custom variables set in an API product. 

## Child element reference

This section describes the child elements of [`<SpikeArrest>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#spikearrest).

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

### `<Identifier>`

Lets you choose how to group the requests so that the SpikeArrest policy can be applied based on the client. For example, you can group requests by developer ID, in which case each developer's requests will count towards their own SpikeArrest rate and not all requests to the proxy.

Use in conjunction with [`<MessageWeight>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#messageweight) element for more fine-grained control over request throttling.

If you leave the `<Identifier>` element empty, one rate limit is enforced for all requests into that API proxy.

**Default Value** | n/a  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SpikeArrest>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#spikearrest)  
**Child Elements** |  None   
  
### Syntax
    
    
    <SpikeArrest
      continueOnError="[false|true]"
      enabled="[true|false]"
      name="policy_name"
    >
    ** <Identifier ref="flow_variable"/>**
    </SpikeArrest>
            

### Example 1

The following example applies the SpikeArrest policy per developer ID:
    
    
    <SpikeArrest name="Spike-Arrest-1">
      <Identifier ref="developer.id"/>
      <Rate>42pm</Rate/>
      <UseEffectiveCount>true</UseEffectiveCount>
    </SpikeArrest>

The following table describes the attributes of `<Identifier>`:

Attribute | Description | Default | Presence  
---|---|---|---  
`ref` | Identifies the variable by which SpikeArrest groups incoming requests. You can use any flow variable to indicate a unique client, such those available with the [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy). You can also set custom variables using the [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) or the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). | n/a | Required  
  
This element is also discussed in [this Apigee Community post](https://www.googlecloudcommunity.com/gc/Apigee/How-does-the-Quota-policy-work-when-no-Identifier-is-specified/td-p/34536).

### `<MessageWeight>`

Specifies the weighting defined for each message. Message weight modifies the impact of a single request on the calculation of the SpikeArrest rate. Message weight can be any flow variable, such as an HTTP header, query parameter, form parameter, or message body content. You can also use custom variables using the [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) or the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

Use in conjunction with [`<Identifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#identifier) to further throttle requests by specific clients or apps.

For example, if the SpikeArrest [`<Rate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate) is `10pm`, and an app submits requests with a weight of `2`, then only five messages per minute are permitted from that client because each request counts as 2.

**Default Value** | n/a  
---|---  
**Required?** | Optional  
**Type** | Integer  
**Parent Element** |  [`<SpikeArrest>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#spikearrest)  
**Child Elements** |  None   
  
### Syntax
    
    
    <SpikeArrest
      continueOnError="[false|true]"
      enabled="[true|false]"
      name="policy_name"
    >
    ** <MessageWeight ref="flow_variable"/>**
    </SpikeArrest>

### Example 1

The following example restricts requests to 12 per minute (one request allowed every five seconds, or 60/12):
    
    
    <SpikeArrest name="SA-With-Dynamic-Weight-1">
      <Rate>12pm</Rate>
      <Identifier ref="client_id" />
      <MessageWeight ref="request_specific_weight" />
      <UseEffectiveCount>true</UseEffectiveCount>
    </SpikeArrest>

In this example, `<MessageWeight>` accepts a custom value (the `weight` header in the request) that adjusts message weights for specific clients. This provides additional control over throttling for entities that are identified with the [`<Identifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#identifier) element.

The following table describes the attributes of `<MessageWeight>`:

Attribute | Description | Presence | Default  
---|---|---|---  
`ref` | Identifies the flow variable that contains the message weight for the specific client. This can be any flow variable, such as an HTTP query param, header, or message body content. For more information, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference). You can also set custom variables using the [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) or the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). | Required | N/A  
  
### `<Rate>`

Specifies the rate at which to limit traffic spikes (or bursts) by setting the number of requests that are allowed in per minute or per second intervals. You can also use this element in conjunction with [`<Identifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#identifier) and [`<MessageWeight>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#messageweight) to smoothly throttle traffic at runtime by accepting values from the client. Use the [`<UseEffectiveCount>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount) element to set the rate limiting algorithm used by the policy.

**Note:** The use of [`<UseEffectiveCount>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount) with a value or `false` is not supported for _any_ Apigee organizations or for Apigee hybrid organizations running production workloads. For more information, see [`<UseEffectiveCount>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#useeffectivecount).

See the [SpikeArrest section of the Limits page](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#spikearrest) for the maximum rate limits you can specify.

**Default Value** | n/a  
---|---  
**Required?** | Required  
**Type** | Integer  
**Parent Element** |  [`<SpikeArrest>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#spikearrest)  
**Child Elements** |  None   
  
### Syntax

You can specify rates in one of the following ways:

  * A static rate that you specify as the body of the `<Rate>` element
  * A variable value, which can be passed by the client; identify the name of the flow variable using the `ref` attribute


    
    
    <SpikeArrest
      continueOnError="[false|true]"
      enabled="[true|false]"
      name="policy_name"
    >
    ** <Rate ref="flow_variable">rate[pm|ps]</Rate>**
    </SpikeArrest>

Valid rate values (either defined as a variable value or in the body of the element) must conform to the following format:

  * `intps` (number of requests per second, smoothed into intervals of milliseconds)
  * `intpm` (number of requests per minute, smoothed into intervals of seconds)



The value of int must be a positive, non-zero integer.

### Example 1

The following example sets the rate to five requests per second:
    
    
    <SpikeArrest name="SA-Static-5ps">
      <Rate>5ps</Rate>
      <UseEffectiveCount>false</UseEffectiveCount>
    </SpikeArrest>

The policy smoothes the rate to one request allowed every 200 _milliseconds_ (1000/5).

### Example 2

The following example sets the rate to 12 requests per minute:
    
    
    <SpikeArrest name="SA-Static-12pm">
      <Rate>12pm</Rate>
      <UseEffectiveCount>true</UseEffectiveCount>
    </SpikeArrest>

This example policy smoothes the rate to one request allowed every five _seconds_ (60/12).

The following table describes the attributes of `<Rate>`:

Attribute | Description | Presence | Default  
---|---|---|---  
`ref` | Identifies a flow variable that specifies the rate. This can be any flow variable, such as an HTTP query parameter, header, or message body content, or a value such as a KVM. For more information, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference). You can also use custom variables using the [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) or the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). If you define both `ref` _and_ the body of this element, the value of `ref` is applied and takes precedence when the flow variable is set in the request. (The reverse is true when the variable identified in `ref` is _not_ set in the request.) For example:
    
    
    <Rate ref="request.header.custom_rate">1pm</Rate>

In this example, if the client does _not_ pass a `custom_rate` header, then the rate for the API proxy is 1 request per minute for all clients. If the client passes a `custom_rate` header, then the rate limit becomes 10 requests per second for all clients on the proxy — until a request without the `custom_rate` header is sent. You can use [`<Identifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#identifier) to group requests to enforce custom rates for different types of clients. If you specify a value for `ref` but do not set the rate in the body of the `<Rate>` element and the client does not pass a value, then the SpikeArrest policy throws an error. | Optional | n/a  
The following table describes the attributes of `Rate` defining the traffic throttling behavior: Attribute | Description  
---|---  
`messagesPerPeriod` | Specifies the number of messages allowed within a defined period. For example, if a policy is configured for '10ps' (10 per second), the `messagesPerPeriod` value would be 10.  
`periodInMicroseconds` | Defines the time period, in microseconds, over which the `messagesPerPeriod` is calculated. For a '10ps' configuration, this value would be 1,000,000, which is equivalent to one second.  
`maxBurstMessageCount` | Represents the maximum number of requests that can be allowed instantly or in a short burst at the beginning of a new interval.  
**Note:** The values and calculations for these attributes can be affected by the number of MPs and whether the `UseEffectiveCount` setting is enabled. For instance, if you set a rate of '10ps' with 10 MPs and `UseEffectiveCount` is enabled, the effective rate for each MP is 1ps. The internal attributes of the individual MP are adjusted to reflect this. For example, the `messagesPerPeriod` attribute could be set to 1 and `periodInMicroseconds` to 1,000,000.

### `<UseEffectiveCount>`

This element lets you choose between distinct spike arrest algorithms by setting the value to `true` or `false`, as explained below:

### true

If set to `true`, SpikeArrest is distributed in a region. That means request counts are synchronized across message processors (MPs) in a region. In addition, a "sliding window" rate limiting algorithm is employed. This algorithm provides consistent rate limit behavior and does not "smooth" the number of incoming requests that can be sent to the backend. If a burst of requests are sent in a short time interval, they are allowed as long as they do not exceed the configured rate limit, as set in the [`<Rate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate) element. For example:
    
    
    <SpikeArrest name="Spike-Arrest-1">
      <Rate>12pm</Rate>
      <Identifier ref="client_id" />
      <MessageWeight ref="request.header.weight" />
      <UseEffectiveCount>true</UseEffectiveCount>
    </SpikeArrest>

### false (default)

**Note:** Although the default value is `false`, Apigee organizations should set this element to `true`. 

Rate smoothing is not supported for Apigee organizations. 

If set to `false` (the default), the SpikeArrest policy uses a "[token bucket](https://en.wikipedia.org/wiki/Token_bucket)" algorithm that smooths traffic spikes by dividing the rate limit that you specify into smaller intervals. A drawback of this approach is that multiple legitimate requests coming in over a short time interval can potentially be denied.

For example, say you enter a rate of 30pm (30 requests per minute). In testing, you might think you could send 30 requests in 1 second, as long as they came within a minute. But that's not how the policy enforces the setting. If you think about it, 30 requests inside a 1-second period could be considered a mini spike in some environments.

  * **Per-minute** rates get smoothed into full requests allowed in intervals of **seconds**.  


For example, 30pm gets smoothed like this:  
60 seconds (1 minute) / 30pm = 2-second intervals, or 1 request allowed every 2 seconds. A second request inside of 2 seconds will fail. Also, a 31st request within a minute will fail.

  * **Per-second** rates get smoothed into full requests allowed in intervals of **milliseconds**. 

For example, 10ps gets smoothed like this:  
1000 milliseconds (1 second) / 10ps = 100-millisecond intervals, or 1 request allowed every 100 milliseconds. A second request inside of 100ms will fail. Also, an 11th request within a second will fail.


**Note:** In rate smoothing, the number of requests is always a whole number greater than zero. Smoothing never involves calculating fractions of requests.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<SpikeArrest>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#spikearrest)  
**Child Elements** |  None   
  
## Flow variables

When a SpikeArrest policy executes, Apigee populates a set of flow variables. You can use these flow variables in conditional flows, or for monitoring and analytics.

**Note:** To check if the SpikeArrest limit has been enforced, use `ratelimit.policy_name.exceed.count > 0` or `ratelimit.policy_name.available.count < 1`. The `ratelimit.policy_name.failed` variable should only be used to detect if the policy itself failed to execute due to an internal error.Variable | Type | Permission | Description  
---|---|---|---  
`ratelimit.policy_name.available.count` | Long | Read-Only | Returns the available SpikeArrest count in the time interval.  
`ratelimit.policy_name.exceed.count` | Long | Read-Only | Returns 1 if the SpikeArrest limit was exceeded in the current time window.  
`ratelimit.policy_name.failed` | Boolean | Read-Only | This variable is `true` if the policy experienced an internal execution failure. This variable should **not** be used to check if a rate limit has been exceeded. It may be set to `true` under high load due to the policy's "fail-open" design.   
  
For more information, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Fault code | HTTP status | Cause | Fix | `policies.ratelimit.FailedToResolveSpikeArrestRate` | `500` | This error occurs if the reference to the variable containing the rate setting within the [`<Rate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate) element cannot be resolved to a value within the `SpikeArrest` policy. This element is mandatory and used to specify the spike arrest rate in the form of `intpm` or `intps`. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/spike-arrest-runtime-errors#failedtoresolvespikearrestrate)  
---|---|---|---  
`policies.ratelimit.InvalidMessageWeight` | `500` | This error occurs if the value specified for the [`<MessageWeight>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#messageweight) element through a flow variable is invalid (a non-integer value). | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/spike-arrest-runtime-errors#invalidmessageweight)  
`policies.ratelimit.SpikeArrestViolation` | `429` | The rate limit is exceeded. |   
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Error name | Cause | Fix  
---|---|---  
`InvalidAllowedRate` | If the spike arrest rate specified in the [`<Rate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate) element of the `SpikeArrest` policy is not an integer or if the rate does not have `ps` or `pm` as a suffix, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/spike-arrest-deployment-errors#invalidallowedrate)  
  
### Fault variables

These variables are set when a runtime error occurs. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "SpikeArrestViolation"`  
`ratelimit.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `ratelimit.SA-SpikeArrestPolicy.failed = true`  
  
### Example error response

Shown below is an example error response:

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {  
       "fault":{  
          "detail":{  
             "errorcode":"policies.ratelimit.SpikeArrestViolation"
          },
          "faultstring":"Spike arrest violation. Allowed rate : 10ps"
       }
    }

### Example fault rule

Shown below is an example fault rule to handle a `SpikeArrestViolation` fault:
    
    
    <FaultRules>
        <FaultRule name="Spike Arrest Errors">
            <Step>
                <Name>Assign-Message-1</Name>
                <Condition>(fault.name Matches "SpikeArrestViolation") </Condition>
            </Step>
            <Condition>(ratelimit.Spike-Arrest-1.exceed.count > 0) or (ratelimit.Spike-Arrest-1.available.count < 1)</Condition>
        </FaultRule>
    </FaultRules>

The current HTTP status code for exceeding a rate limit set by a Quota or SpikeArrest policy is 429 (Too Many Requests).

## Schemas

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

## Related topics

  * [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy): Quota policy, to limit traffic on individual clients
  * [Rate-limiting](https://docs.cloud.google.com/apigee/docs/api-platform/develop/rate-limiting) for a rate limiting overview
  * [Comparing Quota and SpikeArrest policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/comparing-quota-and-spike-arrest-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
