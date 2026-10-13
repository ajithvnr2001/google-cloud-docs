---
url: https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings/
title: localization_settings \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:17.097926+00:00
---

# localization_settings  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  localization_settings Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    localization_settings: {
      localization_level: permissive
      default_locale: en
      import_locale_defs: yes | no
    }
    

Hierarchy [Project Manifest File](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) `localization_settings` |  Default Value None  
---|---  
  
## Definition

By adding localization to your project, you can customize the display of the labels and descriptions in the Looker UI based on a user's locale, and you can also localize certain parts of LookML dashboards. See the [Localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization) documentation page for information about setting up your model for localization.

Use the `localization_settings` parameter to enable localization for your project and to specify how your project handles localization:

  * The `default_locale` parameter specifies the default locale strings file that defines which strings in your model are localized. Enter the exact name of the file (case-sensitive) without the file extension. For example, if the strings file is named `en.strings.json`, you would specify `default_locale: en`. See the [Localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization#strings) documentation page for information about how the locale strings files work.
  * The `localization_level` parameter specifies whether strings with no translation are allowed in your model: 
    * Set the localization level to `strict` if you want the Looker IDE to return a LookML validation error for any labels or descriptions that aren't defined in the default locale strings file.
    * Set the localization level to `permissive` to allow labels and descriptions that aren't defined in the default localization strings file.
  * The `import_locale_defs` parameter specifies whether locale definitions from imported projects should be combined with the importing project's locale definitions: 
    * Set to `yes` to combine locale definitions from imported projects with the importing project's locale definitions.
    * Set to `no` (the default value) to ignore locale definitions from imported projects. Looker will use the locale definitions from the importing project only, if the importing project has locale definitions. 



See the [Localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization) documentation page for more information about the localization settings.

## Example

In a manifest file, specify that the default locale is "en", that localization has a permissive policy, and that locale definitions from imported projects should be combined with the importing project's locale definitions:
    
    
    project_name: "flights"
    
    localization_settings: {
      default_locale: en
      localization_level: permissive
      import_locale_defs: yes
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
