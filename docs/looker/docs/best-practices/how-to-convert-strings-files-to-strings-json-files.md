---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-convert-strings-files-to-strings-json-files/
title: Converting .strings files to .strings.json files \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:48:39.725482+00:00
---

# Converting .strings files to .strings.json files  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-convert-strings-files-to-strings-json-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Converting .strings files to .strings.json files Stay organized with collections  Save and categorize content based on your preferences. 

To support broader language configurations and improve string management within your Looker projects, convert `.strings` files to the `.strings.json` format. This modernization helps you leverage enhanced localization capabilities, making your data applications more accessible and efficient for users across different locales. This guide provides the steps to migrate your existing files. 

To convert a `.strings` file to a `.strings.json` file: 

  1. If you're using a Looker version prior to 7.12, turn off the **Legacy .strings files for localization** legacy feature.
  2. Create a new `.strings.json` file for your project by clicking the **+** icon at the top right of your project file list and selecting **Create Locale Strings File**.
  3. Name your new `.strings.json` file. The titles of `.strings` files must [match the locale code](https://docs.cloud.google.com/looker/docs/model-localization#assigning_users_to_a_locale) assigned to users or groups who are using that locale, and the title of the default locale file must match the value for the `default_locale` in your project's [manifest file](https://docs.cloud.google.com/looker/docs/model-localization#manifest).
  4. The snippet that appears in the new `.strings.json` file provides an example of JSON formatting. Delete this example and replace it with a pair of curly braces: `{}`
  5. Copy the key-value pairs from your old `.strings` file and paste them inside the curly braces.
  6. Replace all the equal signs with colons.
  7. Remove any comments; or reformat them as individual comments or as an array of comments, as illustrated next.
  8. Replace all the semicolons with commas.



Typical `.strings.json` formatting of the key-value pairs looks like this: 
    
    
    {
        "flight_info" : "Flight Info",
        "id" : "Identifier",
        "airline" : "Air Carrier"
    }
    

To format comments, you can use these formats: 
    
    
    {
        " My Comment": {
            "my_comment_array": [
            "The name of this file should be the associated locale code followed by '.strings.json'",
            "There is one .strings.json file per locale.",
            "Define your translated strings one key at a time",
            "Keys can be any string; choose whatever scheme helps you stay organized",
            "Then, set your Lookml label and description parameters to the desired key values.",
            "To choose this file as the master key list and as the one to validate against",
            "set its locale code ('test') as the default_locale in the manifest file"
            ],
            "value": "Translation for My Comment"
        },
        "My Key": {
            "value": "Translation for My Key",
            "comment": "Define your translated strings with a comment or an array of comments"
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
