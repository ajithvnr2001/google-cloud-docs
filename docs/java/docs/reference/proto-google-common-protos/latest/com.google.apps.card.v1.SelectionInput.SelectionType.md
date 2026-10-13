---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.SelectionInput.SelectionType
title: Enum SelectionInput.SelectionType (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:59.654654+00:00
---

# Enum SelectionInput.SelectionType (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.SelectionInput.SelectionType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum SelectionInput.SelectionType (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public enum SelectionInput.SelectionType extends Enum<SelectionInput.SelectionType> implements ProtocolMessageEnum

The format for the items that users can select. Different options support different types of interactions. For example, users can select multiple checkboxes, but can only select one item from a dropdown menu.

Each selection input supports one type of selection. Mixing checkboxes and switches, for example, isn't supported.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

Protobuf enum `google.apps.card.v1.SelectionInput.SelectionType`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`CHECK_BOX` |  A set of checkboxes. Users can select one or more checkboxes. `CHECK_BOX = 0;`  
`CHECK_BOX_VALUE` |  A set of checkboxes. Users can select one or more checkboxes. `CHECK_BOX = 0;`  
`DROPDOWN` |  A dropdown menu. Users can select one item from the menu. For Google Chat apps, you can populate items using a dynamic data source and autosuggest items as users type in the menu. For example, users can start typing the name of a Google Chat space and the widget autosuggests the space. To dynamically populate items for a dropdown menu, use one of the following types of data sources:

  * Google Workspace data: Items are populated using data from Google Workspace, such as Google Workspace users or Google Chat spaces.
  * External data: Items are populated from an external data source outside of Google Workspace. For examples of how to implement dropdown menus for Chat apps, see [Add a dropdown menu](https://developers.google.com/workspace/chat/design-interactive-card-dialog#dropdown-menu) and [Dynamically populate drop-down menus](https://developers.google.com/workspace/chat/design-interactive-card-dialog#dynamic-dropdown-menu). [Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`DROPDOWN = 3;`  
`DROPDOWN_VALUE` |  A dropdown menu. Users can select one item from the menu. For Google Chat apps, you can populate items using a dynamic data source and autosuggest items as users type in the menu. For example, users can start typing the name of a Google Chat space and the widget autosuggests the space. To dynamically populate items for a dropdown menu, use one of the following types of data sources:

  * Google Workspace data: Items are populated using data from Google Workspace, such as Google Workspace users or Google Chat spaces.
  * External data: Items are populated from an external data source outside of Google Workspace. For examples of how to implement dropdown menus for Chat apps, see [Add a dropdown menu](https://developers.google.com/workspace/chat/design-interactive-card-dialog#dropdown-menu) and [Dynamically populate drop-down menus](https://developers.google.com/workspace/chat/design-interactive-card-dialog#dynamic-dropdown-menu). [Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`DROPDOWN = 3;`  
`MULTI_SELECT` |  A menu with a text box. Users can type and select one or more items. For Google Workspace add-ons, you must populate items using a static array of `SelectionItem` objects. For Google Chat apps, you can also populate items using a dynamic data source and autosuggest items as users type in the menu. For example, users can start typing the name of a Google Chat space and the widget autosuggests the space. To dynamically populate items for a multiselect menu, use one of the following types of data sources:

  * Google Workspace data: Items are populated using data from Google Workspace, such as Google Workspace users or Google Chat spaces.
  * External data: Items are populated from an external data source outside of Google Workspace. For examples of how to implement multiselect menus for Chat apps, see [Add a multiselect menu](https://developers.google.com/workspace/chat/design-interactive-card-dialog#multiselect-menu). [Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`MULTI_SELECT = 4;`  
`MULTI_SELECT_VALUE` |  A menu with a text box. Users can type and select one or more items. For Google Workspace add-ons, you must populate items using a static array of `SelectionItem` objects. For Google Chat apps, you can also populate items using a dynamic data source and autosuggest items as users type in the menu. For example, users can start typing the name of a Google Chat space and the widget autosuggests the space. To dynamically populate items for a multiselect menu, use one of the following types of data sources:

  * Google Workspace data: Items are populated using data from Google Workspace, such as Google Workspace users or Google Chat spaces.
  * External data: Items are populated from an external data source outside of Google Workspace. For examples of how to implement multiselect menus for Chat apps, see [Add a multiselect menu](https://developers.google.com/workspace/chat/design-interactive-card-dialog#multiselect-menu). [Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`MULTI_SELECT = 4;`  
`RADIO_BUTTON` |  A set of radio buttons. Users can select one radio button. `RADIO_BUTTON = 1;`  
`RADIO_BUTTON_VALUE` |  A set of radio buttons. Users can select one radio button. `RADIO_BUTTON = 1;`  
`SWITCH` |  A set of switches. Users can turn on one or more switches. `SWITCH = 2;`  
`SWITCH_VALUE` |  A set of switches. Users can turn on one or more switches. `SWITCH = 2;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.SelectionInput.SelectionType#com_google_apps_card_v1_SelectionInput_SelectionType_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
