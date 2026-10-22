---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy/
title: PublishMessage policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:10.710161+00:00
---

# PublishMessage policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  PublishMessage policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The PublishMessage policy lets you publish your API proxy flow information to a Google Cloud Pub/Sub topic. Google's Pub/Sub allows services to communicate asynchronously, with significantly less latency. For more information about Pub/Sub, see [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview). The information you want to publish to a Pub/Sub topic can be a literal text or a flow variable. You can also specify a combination of literal text and flow variables by using a [message template](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).

If the publish request is successful, Apigee sets the `publishmessage.message.id` flow variable to the value returned by the Pub/Sub server. For more information, see Flow variables.

**Note:**

  * You can publish a message to only one topic by using the PublishMessage policy. If you want to publish a message to multiple topics, use multiple PublishMessage policies (one policy for each topic).
  * To run the PublishMessage policy, you should enable the Pub/Sub APIs for your Google Cloud project. For more information about enabling APIs for a Google Cloud project, see [Enabling and Disabling Services](https://docs.cloud.google.com/service-usage/docs/enable-disable).



This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## Authentication and proxy deployment

To run the PublishMessage policy, you need an authentication token. However, there is no explicit <Authentication> element in the policy definition. You must deploy your API proxy to use Google authentication, which adds the authentication token to the request under the hood. For information on how to deploy an API proxy that uses Google authentication, see [Deployment steps](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview#deployment-steps).

You must deploy your API proxy with a service account that has a role with the `pubsub.topics.publish` permission. For more information about Identity and Access Management (Identity and Access Management (IAM)) roles for Pub/Sub, see [Permissions and roles](https://docs.cloud.google.com/pubsub/docs/access-control).

The service account should also have the `roles/iam.serviceAccountTokenCreator` role in order to generate the token for the proxy service account. See [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) for more information.

## `<PublishMessage>`

Specifies the PublishMessage policy.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  N/A   
**Child Elements** |  [`<Attributes>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#attributes)  
[`<CloudPubSub>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#cloudpubsub)  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#displayname)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#ignoreunresolvvars)  
[`<Source>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#source)  
[`<UseMessageAsSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#umas)  
  
  
The following table provides a high-level description of the child elements of [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage): 

Child Element | Required? | Description  
---|---|---  
[`<Attributes>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#attributes) | Optional | A set of attributes to attach to the Pub/Sub message.  
[`<CloudPubSub>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#cloudpubsub) | Required | Parent element of [`<Topic>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#topic). The `<Topic>` element specifies the Pub/Sub topic in which you want to publish your message.  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#displayname) | Optional | A custom name for the policy.  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#ignoreunresolvvars) | Optional | Specifies whether processing stops if Apigee encounters an unresolved variable.  
[`<Source>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#source) | Optional | Specifies the message to publish to the Pub/Sub topic. This element is optional, but you must use either `<Source>` or `<UseMessageAsSource>`.   
[`<UseMessageAsSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#umas) | Optional | Specifies the message to publish to the Pub/Sub topic. This element is optional, but you must use either `<Source>` or `<UseMessageAsSource>`.   
Other child elements  
[`<Topic>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#topic) | Required | A child element of `<CloudPubSub>`. Specifies the Pub/Sub topic to which you want to publish the message.  
[`<Endpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#endpoint) | Optional | A child element of `<CloudPubSub>`. Specifies the regional endpoint for Pub/Sub messaging to support [advanced data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-advanced-data-residency). Defaults to the global endpoint `pubsub.googleapis.com:443` if not specified.  
  
The `<PublishMessage>` element uses the following syntax:

### Syntax
    
    
    <PublishMessage continueOnError="[true|false]" enabled="[true|false]" name="Publish-Message-1">
        <DisplayName>DISPLAY_NAME</DisplayName>
        <Source>SOURCE_VALUE</Source>
        <Attributes>
            <Attribute> name=ATTRIBUTE_NAME>ATTRIBUTE_VALUE</Attribute>
        </Attributes>
        <CloudPubSub>
            <Topic>TOPIC_NAME</Topic>
            <Endpoint>REGIONAL_ENDPOINT</Endpoint>
        </CloudPubSub>
        <IgnoreUnresolvedVariables>[true|false]</IgnoreUnresolvedVariables>
    </PublishMessage>

### Example - Source

The following example shows the `<PublishMessage>` policy definition:
    
    
    <PublishMessage continueOnError="false" enabled="true" name="Publish-Message-1">
        <DisplayName>Publish Message-1</DisplayName>
        <Source>this is a message template {flow-variable1}</Source>
        <CloudPubSub>
            <Topic>projects/{flow-variable-project-id}/topics/{flow-variable-topic-name}</Topic>
        </CloudPubSub>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </PublishMessage>

### Example - UseMessageAsSource

This `<PublishMessage>` policy specifies the `UseMessageAsSource` element:
    
    
    <PublishMessage continueOnError="false" enabled="true" name="Publish-Message-2">
        <UseMessageAsSource>request</UseMessageAsSource>
        <CloudPubSub>
            <Topic>projects/{flow-variable-project-id}/topics/{flow-variable-topic-name}</Topic>
        </CloudPubSub>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </PublishMessage>

### Example - Attributes

This `<PublishMessage>` policy specifies the `Attributes` element:
    
    
    <PublishMessage name="Publish-Message-3">
      <Source>this is a message template {flow-variable1}</Source>
      <Attributes>
        <Attribute name='attr-name-0'>fixed-value</Attribute>
        <Attribute name='another-attribute-name'>{request.queryparam.attr1}</Attribute>
        <Attribute name='a-third-attribute-name'>{request.queryparam.attr2:default-value}</Attribute>
      </Attributes>
      <CloudPubSub>
        <Topic>projects/{flow-variable-project-id}/topics/{flow-variable-topic-name}</Topic>
      </CloudPubSub>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </PublishMessage>

### Example - Data residency

This `<PublishMessage>` policy specifies the `Endpoint` element:
    
    
    <PublishMessage name="Publish-Message-3">
      <Source>this is a message template {flow-variable1}</Source>
      <CloudPubSub>
        <Topic>projects/{flow-variable-project-id}/topics/{flow-variable-topic-name}</Topic>
        <Endpoint>pubsub.us.rep.googleapis.com:443</Endpoint>
      </CloudPubSub>
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
    </PublishMessage>

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

This section describes the child elements of [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage). 

### `<Attributes>`

Specifies the attributes to attach to the Pub/Sub message.

Each attribute is a key-value pair. The name associated to the attribute should be unique. The value for each is determined dynamically at runtime via a [message template](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage)  
  
**Child Elements** |  None   
  
The `<Attributes>` element uses the following syntax:

#### Syntax
    
    
      <Attributes>
        <Attribute name='NAME-1'>fixed-value</Attribute>
        <Attribute name='NAME-2'>{flow-variable}</Attribute>
        ...
        <Attribute name='NAME-N'>message template here {flow-variable:default-value}</Attribute>
      </Attributes>

#### Example 1

The following example sets a single attribute with a fixed value on the message as it is published:
    
    
    <PublishMessage name="PM-with-one-attribute">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <Source>{request.queryparam.message}</Source>
      **< Attributes>
        <Attribute name='my-attribute-1'>fixed-value</Attribute>
      </Attributes>**
      <CloudPubSub>
        <Topic>projects/{request.queryparam.project}/topics/{request.queryparam.topic}</Topic>
      </CloudPubSub>
    </PublishMessage>

#### Example 2

The following example sets multiple attributes on the message as it is published; the values of some of them are dynamically determined at runtime:
    
    
    <PublishMessage name="PM-with-multiple-attributes">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <Source>{my-assembled-message}</Source>
      **< Attributes>
        <Attribute name='attr-0'>fixed-value</Attribute>
        <Attribute name='attr-1'>{flow-variable1}</Attribute>
        <Attribute name='attr-2'>fixed portion {flow-variable2:default-value}</Attribute>
      </Attributes>**
      <CloudPubSub>
        <Topic>projects/{propertyset.settings.project}/topics/{propertyset.settings.topic}</Topic>
      </CloudPubSub>
    </PublishMessage>

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

### `<Source>`

Specifies the message to publish.

The message can be a literal text, a flow variable, or a combination of both in the form of a [message template](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage)  
  
**Child Elements** |  None   
  
The `<Source>` element uses the following syntax:

#### Syntax
    
    
     <Source>SOURCE</Source>

#### Example-1

The following example sets the source message to the value of the `flow-var-1` flow variable:
    
    
    <Source>{flow-var-1}</Source>

#### Example-2

The following example uses a message template to publish a JSON message with dynamic content:
    
    
    <PublishMessage name="PM-with-source-template">
      **< Source>{
        "name": "value-1",
        "count": "{flow-variable1}",
        "action": "{flow-variable2}"
      }</Source>**
      <Attributes>
        <Attribute name='content-type'>application/json</Attribute>
      </Attributes>
      <CloudPubSub>
        <Topic>projects/{propertyset.settings.project}/topics/{propertyset.settings.topic}</Topic>
      </CloudPubSub>
    </PublishMessage>

### `<CloudPubSub>`

Parent element of [`<Topic>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#topic).

You can publish to only one Pub/Sub topic. Hence, you can have only one `<Topic>` element in the `<CloudPubSub>` element.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex type  
**Parent Element** |  [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage)  
  
**Child Elements** |  [`<Topic>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#topic)  
[`<Endpoint>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#endpoint)  
  
  
The `<CloudPubSub>` element uses the following syntax:

#### Syntax
    
    
    <CloudPubSub>
      <Topic>TOPIC_NAME</Topic>
      <Endpoint>REGIONAL_ENDPOINT</Endpoint>
    </CloudPubSub>

#### Example

The following example shows the declaration of the `<CloudPubSub>` element:
    
    
    <CloudPubSub>
      <Topic>projects/{my-project}/topics/{my-topic}</Topic>
      <Endpoint>pubsub.us.rep.googleapis.com:443</Endpoint>
    </CloudPubSub>

### `<Topic>`

Specifies the Pub/Sub topic to which you want to publish the [`<Source>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#source) message.

Use the following format: `projects/project-id/topics/topic-name`

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<CloudPubSub>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#cloudpubsub)  
  
**Child Elements** |  None   
  
The `<Topic>` element uses the following syntax:

##### Syntax
    
    
    <Topic>TOPIC_NAME</Topic>

##### Example

The following example specifies the Pub/Sub topic to publish to:
    
    
    <Topic>projects/project-id-marketing/topics/topic-name-test1</Topic>

In this example, `project-id-marketing` is your Google Cloud Project ID and `topic-name-test1` is the topic in which the message should be published.

### `<Endpoint>`

Specifies the regional endpoint for Pub/Sub messaging to support [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). **Default Value** | pubsub.googleapis.com:443 (global endpoint)  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<CloudPubSub>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#cloudpubsub)  
  
**Child Elements** |  None   
  
The `<Endpoint>` element uses the following syntax:

##### Syntax
    
    
    <Endpoint>pubsub.CONTROL_PLANE_LOCATION.rep.googleapis.com:443</Endpoint>

**Important:** When using VPC Service Controls with data residency, you must use the following regional endpoint: `CONTROL_PLANE_LOCATION-pubsub.googleapis.com:443`. 

Where **CONTROL_PLANE_LOCATION** is the physical location at which Apigee control plane data will be stored. For a list of available control plane locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#control-plane-location). 

##### Example

The following example specifies the regional endpoint URL to use for Pub/Sub messaging in the US to support data residency:
    
    
    <Endpoint>pubsub.us.rep.googleapis.com:443</Endpoint>

##### Example - With VPC Service Controls

The following example specifies the regional endpoint URL to use for Pub/Sub messaging in the US to support data residency with VPC Service Controls:
    
    
    <Endpoint>us-pubsub.googleapis.com:443</Endpoint>

### `<UseMessageAsSource>`

Specifies the message to publish.

Use this as an alternative to the `<Source>` element. The value should be the name of a flow variable referring to a message, such as `request`, `response`, or `message`. When you specify this element, the policy uses the content of the message as the message to publish. You should use this element rather than `<Source>` when the message content is an octet stream which cannot be represented as a string, for example content from a binary file. 

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage)  
  
**Child Elements** |  None   
  
The `<UseMessageAsSource>` element uses the following syntax:

#### Syntax
    
    
    <PublishMessage name="PM-with-use-message-as-source">
      **< UseMessageAsSource>MESSAGE_NAME</UseMessageAsSource>**
      <Attributes>
        <Attribute name='attr-1'>{flowvar1}</Attribute>
      </Attributes>
      <CloudPubSub>
        <Topic>projects/{flowvar1}/topics/{flowvar-topic}</Topic>
      </CloudPubSub>
    </PublishMessage>

#### Example-1

The following example tells the policy to use the content of the request message as the payload for the Pub/Sub message:
    
    
    <PublishMessage name="PM-with-use-message-as-source">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      **< UseMessageAsSource>request</UseMessageAsSource>**
      <Attributes>
        <Attribute name='attr-1'>{flowvar1}</Attribute>
      </Attributes>
      <CloudPubSub>
        <Topic>projects/{propertyset.settings.project}/topics/{propertyset.settings.topic}</Topic>
      </CloudPubSub>
    </PublishMessage>

### `<IgnoreUnresolvedVariables>`

Specifies whether processing stops if Apigee encounters an unresolved variable.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage)  
**Child Elements** |  None   
  
Set the value to `true` to ignore unresolved variables and continue processing; otherwise `false`. The default value is `false`.

Setting `<IgnoreUnresolvedVariables>` to `true` is different from setting the [`<PublishMessage>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#publishmessage)'s `continueOnError` to `true`. If you set `continueOnError` to `true`, Apigee ignores all errors, not only errors in variables.

The `<IgnoreUnresolvedVariables>` element uses the following syntax:

### Syntax
    
    
    <IgnoreUnresolvedVariables>[true|false]</IgnoreUnresolvedVariables>

### Example

The following example sets `<IgnoreUnresolvedVariables>` to `true`:
    
    
    <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>

## Flow variables

Flow variables are objects that hold specific data and are available to you in the context of an API proxy flow. These variables store information such as payload information, URL path, IP addresses, and data from policy execution. For more information about flow variables, see [Using flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables). 

If the PublishMessage policy successfully publishes to the Pub/Sub topic, Apigee sets the `[publishmessage.message.id](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#publishmessage)` flow variable to the [messageId](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) returned by the Pub/Sub server. The flow variable is of type string, and the variable is available to you from the Proxy request flow onwards. Based on your requirement, you can use the flow variable in other downstream policies. However, if the publish fails, Apigee does not set the `publishmessage.message.id` variable, and accessing this variable will cause errors. 

For more information about various types of flow variables, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause  
---|---|---  
`steps.publishmessage.PermissionDeniedError` | `500` | This error occurs when the runtime service account cannot impersonate the proxy service account or the proxy service account does not have the permission to publish to the topic.  
`steps.publishmessage.ExecutionError` | `500` | This error occurs if there was an unexpected error while publishing the message to Pub/Sub. You can view the details of the error in the error message.   
`steps.publishmessage.MessageVariableNotMessageType` | `500` | This error occurs if the variable name you specified in `UseMessageAsSource` cannot be resolved, or is not a message type.   
  
### Fault variables

Whenever there are execution errors in a policy, Apigee generates error messages. You can view these error messages in the error response. Many a time, system generated error messages might not be relevant in the context of your product. You might want to customize the error messages based on the type of error to make the messages more meaningful.

To customize the error messages, you can use either fault rules or the RaiseFault policy. For information about differences between fault rules and the RaiseFault policy, see [FaultRules vs. the RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#rulesvraisefault). You must check for conditions using the `Condition` element in both the fault rules and the RaiseFault policy. Apigee provides fault variables unique to each policy and the values of the fault variables are set when a policy triggers runtime errors. By using these variables, you can check for specific error conditions and take appropriate actions. For more information about checking error conditions, see [Building conditions](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#buildingconditions).

Variables | Where | Example  
---|---|---  
`fault.name` | The `fault.name` can match to any of the faults listed in the Runtime errors table. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`publishmessage.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `publishmessage.publish-message-1.failed = true`  
For more information about policy errors, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
