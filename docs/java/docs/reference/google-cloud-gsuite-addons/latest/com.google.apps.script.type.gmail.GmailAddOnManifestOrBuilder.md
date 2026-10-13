---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.GmailAddOnManifestOrBuilder
title: Interface GmailAddOnManifestOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:21.525847+00:00
---

# Interface GmailAddOnManifestOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.GmailAddOnManifestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GmailAddOnManifestOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.6  2.2.1  2.1.12 
    
    
    public interface GmailAddOnManifestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthorizationCheckFunction()
    
    
    public abstract String getAuthorizationCheckFunction()

The name of an endpoint that verifies that the add-on has all the required third-party authorizations, by probing the third-party APIs. If the probe fails, the function should throw an exception to initiate the authorization flow. This function is called before each invocation of the add-on, in order to ensure a smooth user experience.

`string authorization_check_function = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The authorizationCheckFunction.  
  
### getAuthorizationCheckFunctionBytes()
    
    
    public abstract ByteString getAuthorizationCheckFunctionBytes()

The name of an endpoint that verifies that the add-on has all the required third-party authorizations, by probing the third-party APIs. If the probe fails, the function should throw an exception to initiate the authorization flow. This function is called before each invocation of the add-on, in order to ensure a smooth user experience.

`string authorization_check_function = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for authorizationCheckFunction.  
  
### getComposeTrigger()
    
    
    public abstract ComposeTrigger getComposeTrigger()

Defines the compose time trigger for a compose time add-on. This is the trigger that causes an add-on to take action when the user is composing an email. All compose time addons are required to have the gmail.addons.current.action.compose scope even though it might not edit the draft.

`.google.apps.script.type.gmail.ComposeTrigger compose_trigger = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ComposeTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.ComposeTrigger)` | The composeTrigger.  
  
### getComposeTriggerOrBuilder()
    
    
    public abstract ComposeTriggerOrBuilder getComposeTriggerOrBuilder()

Defines the compose time trigger for a compose time add-on. This is the trigger that causes an add-on to take action when the user is composing an email. All compose time addons are required to have the gmail.addons.current.action.compose scope even though it might not edit the draft.

`.google.apps.script.type.gmail.ComposeTrigger compose_trigger = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ComposeTriggerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.ComposeTriggerOrBuilder)` |   
  
### getContextualTriggers(int index)
    
    
    public abstract ContextualTrigger getContextualTriggers(int index)

Defines the set of conditions that trigger the add-on.

`repeated .google.apps.script.type.gmail.ContextualTrigger contextual_triggers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContextualTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.ContextualTrigger)` |   
  
### getContextualTriggersCount()
    
    
    public abstract int getContextualTriggersCount()

Defines the set of conditions that trigger the add-on.

`repeated .google.apps.script.type.gmail.ContextualTrigger contextual_triggers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getContextualTriggersList()
    
    
    public abstract List<ContextualTrigger> getContextualTriggersList()

Defines the set of conditions that trigger the add-on.

`repeated .google.apps.script.type.gmail.ContextualTrigger contextual_triggers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ContextualTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.ContextualTrigger)>` |   
  
### getContextualTriggersOrBuilder(int index)
    
    
    public abstract ContextualTriggerOrBuilder getContextualTriggersOrBuilder(int index)

Defines the set of conditions that trigger the add-on.

`repeated .google.apps.script.type.gmail.ContextualTrigger contextual_triggers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContextualTriggerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.ContextualTriggerOrBuilder)` |   
  
### getContextualTriggersOrBuilderList()
    
    
    public abstract List<? extends ContextualTriggerOrBuilder> getContextualTriggersOrBuilderList()

Defines the set of conditions that trigger the add-on.

`repeated .google.apps.script.type.gmail.ContextualTrigger contextual_triggers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.script.type.gmail.ContextualTriggerOrBuilder>` |   
  
### getHomepageTrigger()
    
    
    public abstract HomepageExtensionPoint getHomepageTrigger()

Defines an endpoint that will be executed in contexts that don't match a declared contextual trigger. Any cards generated by this function will always be available to the user, but may be eclipsed by contextual content when this add-on declares more targeted triggers.

If present, this overrides the configuration from `addOns.common.homepageTrigger`.

`.google.apps.script.type.HomepageExtensionPoint homepage_trigger = 14;`

**Returns**  
---  
**Type** | **Description**  
`[HomepageExtensionPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.HomepageExtensionPoint)` | The homepageTrigger.  
  
### getHomepageTriggerOrBuilder()
    
    
    public abstract HomepageExtensionPointOrBuilder getHomepageTriggerOrBuilder()

Defines an endpoint that will be executed in contexts that don't match a declared contextual trigger. Any cards generated by this function will always be available to the user, but may be eclipsed by contextual content when this add-on declares more targeted triggers.

If present, this overrides the configuration from `addOns.common.homepageTrigger`.

`.google.apps.script.type.HomepageExtensionPoint homepage_trigger = 14;`

**Returns**  
---  
**Type** | **Description**  
`[HomepageExtensionPointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.HomepageExtensionPointOrBuilder)` |   
  
### getUniversalActions(int index)
    
    
    public abstract UniversalAction getUniversalActions(int index)

Defines set of [universal actions](https://docs.cloud.google.com/gmail/add-ons/how-tos/universal-actions) for the add-on. The user triggers universal actions from the add-on toolbar menu.

`repeated .google.apps.script.type.gmail.UniversalAction universal_actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UniversalAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.UniversalAction)` |   
  
### getUniversalActionsCount()
    
    
    public abstract int getUniversalActionsCount()

Defines set of [universal actions](https://docs.cloud.google.com/gmail/add-ons/how-tos/universal-actions) for the add-on. The user triggers universal actions from the add-on toolbar menu.

`repeated .google.apps.script.type.gmail.UniversalAction universal_actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUniversalActionsList()
    
    
    public abstract List<UniversalAction> getUniversalActionsList()

Defines set of [universal actions](https://docs.cloud.google.com/gmail/add-ons/how-tos/universal-actions) for the add-on. The user triggers universal actions from the add-on toolbar menu.

`repeated .google.apps.script.type.gmail.UniversalAction universal_actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UniversalAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.UniversalAction)>` |   
  
### getUniversalActionsOrBuilder(int index)
    
    
    public abstract UniversalActionOrBuilder getUniversalActionsOrBuilder(int index)

Defines set of [universal actions](https://docs.cloud.google.com/gmail/add-ons/how-tos/universal-actions) for the add-on. The user triggers universal actions from the add-on toolbar menu.

`repeated .google.apps.script.type.gmail.UniversalAction universal_actions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UniversalActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gsuite-addons/latest/com.google.apps.script.type.gmail.UniversalActionOrBuilder)` |   
  
### getUniversalActionsOrBuilderList()
    
    
    public abstract List<? extends UniversalActionOrBuilder> getUniversalActionsOrBuilderList()

Defines set of [universal actions](https://docs.cloud.google.com/gmail/add-ons/how-tos/universal-actions) for the add-on. The user triggers universal actions from the add-on toolbar menu.

`repeated .google.apps.script.type.gmail.UniversalAction universal_actions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.script.type.gmail.UniversalActionOrBuilder>` |   
  
### hasComposeTrigger()
    
    
    public abstract boolean hasComposeTrigger()

Defines the compose time trigger for a compose time add-on. This is the trigger that causes an add-on to take action when the user is composing an email. All compose time addons are required to have the gmail.addons.current.action.compose scope even though it might not edit the draft.

`.google.apps.script.type.gmail.ComposeTrigger compose_trigger = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the composeTrigger field is set.  
  
### hasHomepageTrigger()
    
    
    public abstract boolean hasHomepageTrigger()

Defines an endpoint that will be executed in contexts that don't match a declared contextual trigger. Any cards generated by this function will always be available to the user, but may be eclipsed by contextual content when this add-on declares more targeted triggers.

If present, this overrides the configuration from `addOns.common.homepageTrigger`.

`.google.apps.script.type.HomepageExtensionPoint homepage_trigger = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the homepageTrigger field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
