---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-html-widget/
title: Configure the HTML widget \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:58.943319+00:00
---

# Configure the HTML widget  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-html-widget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure the HTML widget

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The **HTML** widget lets you define the content and style of the displayed data. You can customize it using a variety of presets, including ready-made HTML code to display the data in a predefined format. You can further personalize the display with the code editor, which provides a tailored view of the data in the case or alert overview. 

The HTML widget comes with the following presets:

  * Empty
  * Clock
  * Map
  * Table
  * Video
  * Number
  * Score
  * Bar Chart
  * Conversation
  * Gallery
  * User Details
  * 7 Layout options

**Note:** When you use the **Video** or **Layout** presets, certain video sites, such as YouTube and files.fm, aren't supported. We recommend that you use Sendspark as an alternative. If you're unsure whether the video site you're using is supported within the Google Security Operations platform, contact [Customer Support](https://docs.cloud.google.com/chronicle/docs/getting-support) . 

## Create an HTML widget

To create an HTML widget that displays enrichment details about the target user in a phishing use case, follow these steps:

  1. On the **Playbooks** page, drag the **HTML** widget in the view.
  2. Click  settings  **Settings** and configure it with the relevant information. For this example, name the widget _Target Profile_. 
  3. Select **User Details**.
  4. Select **Empty** to customize your widget. This preset doesn't contain any predefined HTML code.
  5. Define the optimal height of the widget. For this example, keep the default widget height as 425 pixels.
  6. You can click the **Safe HTML Rendering** toggle to activate safe HTML rendering, returning code without potentially malicious JavaScript.
  7. Highlight and customize the field/value in the preconfigured HTML code provided by the preset. Click  to expand the code editor window.
  8. Click  data_array  **Data Array** to insert placeholders in the code.
  9. Select the required value for each field from the list.
  10. In this example, replace the fields with the following values from the playbook:**Variable**  
  
| **Value**  
  
  
---|---  
`Var field2 =`| `[Entity.AD_Image]`  
`Var field3 =`| `[Entity.Ad_Displayname]`  
`Var field4 =`| `[Entity.AD_role]`  
`Var field5 =`| `[Environment.ContactEmail]`  
`Var field6 =`| `[Entity.AD_address]`  
`Var field7=`| `[Entity.AD_Displayname]`  
`Var field8=`| `[Entity.AD_memberOf]`  
`Var field9=`| `[Entity.IsFromLdapString]`  
`Var field10=`| `[Entity.Environment]`  
  

  11. Click **Save**. As data is ingested into the Google SecOps platform, the HTML widget populates with information captured during the playbook run.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
