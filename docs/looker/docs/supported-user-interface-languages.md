---
url: https://docs.cloud.google.com/looker/docs/supported-user-interface-languages/
title: Supported user-interface languages \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:54:11.754575+00:00
---

# Supported user-interface languages  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/supported-user-interface-languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Supported user-interface languages Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** User-interface language is often selected in conjunction with model and number format localization. To learn more about those topics, visit the [Localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization) and [Localizing number formatting](https://docs.cloud.google.com/looker/docs/localizing-number-formatting) documentation pages.

Looker admins can set Looker to display certain user interface (UI) text in the following languages:

Language | Locale Code and Strings Filename  
---|---  
English | `en`  
Czech | `cs_CZ`  
German | `de_DE`  
Spanish (Spain) | `es_ES`  
Finnish | `fi_FI`  
French (Canada) | `fr_CA`  
French (France) | `fr_FR`  
Hindi | `hi_IN`  
Italian | `it_IT`  
Japanese | `ja_JP`  
Korean | `ko_KR`  
Lithuanian | `lt_LT`  
Norwegian (Bokmål) | `nb_NO`  
Dutch | `nl_NL`  
Polish | `pl_PL`  
Brazilian Portuguese | `pt_BR`  
Portuguese | `pt_PT`  
Russian | `ru_RU`  
Swedish | `sv_SE`  
Thai | `th_TH`  
Turkish | `tr_TR`  
Ukrainian | `uk_UA`  
Simplified Chinese | `zh_CN`  
Traditional Chinese | `zh_TW`  
  
To display the Looker UI in specific languages for particular users, set the locale for users, user groups, or instances through one of the following methods:

  * **To set a locale for individual users:** Use one of the codes from the supported user-interface languages table in the [**Locale** field](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#locale) on the **Edit User** page in the **Admin** panel.
  * **To set a locale for a user group:** Assign one of the codes from the supported user-interface languages table to the `locale` user attribute for [a particular user group](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups). If users within a group have set a custom value using the **Locale** setting, the custom value will override any value assigned to the group. To prevent that from happening, ensure that the **User Access** setting for the `locale` user attribute is not set to **Edit**.
  * **To set a locale for an instance:** Assign one of the codes from the supported user-interface languages table to the **Locale** field on the [**Localization** page](https://docs.cloud.google.com/looker/docs/admin-panel-general-localization) of the **Admin** panel.



For users with no **Locale** set, Looker uses the locale chosen on the **Localization** page of the **Admin** panel as the default locale; and, if no locale is set there, Looker defaults to `en`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
