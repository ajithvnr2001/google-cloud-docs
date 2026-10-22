---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields/
title: Create custom fields for cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:30.670035+00:00
---

# Create custom fields for cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create custom fields for cases

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document describes how to create and manage custom fields, and how to use them for [advanced reporting](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields#use-custom-fields-advanced-reports). Custom fields let administrators add specific information to cases and alerts. You can organize these custom fields using a **Custom Fields Form** widget, which defines the default views for cases and alerts. Analysts can then enter information directly into this widget from the **Overview** tab of cases and alerts, based on the custom field's configured scope.

## Create a custom field

Administrators can create up to 1,000 custom fields. Once a custom field is saved, you can't modify its **Scope** , **Type** , or **Name**. To create a custom field, do the following:

  1. Go to **SOAR Settings > Case Data > Custom Fields**.
  2. Click  Add **Add** to create a new custom field.
  3. Select **Scope** and then select **Case** , **Alert** , or **All** (both). The **Scope** field is required and can't be changed once the custom field is created.
  4. Enter a custom field **Name**. The **Name** field is required and can't be changed after the custom field is created.
  5. In the list, select a custom field **Type** :

     * **Free Text** : Enter any text, up to 1,024 characters.
     * **Radio Button** : Provides two customizable options for selection.
     * **Single Select** : List with a single option to select. This type supports a maximum of 1,024 characters, with each option name limited to 255 characters.
     * **Multi Select** : List with multiple options to select. This type supports a maximum of 1,024 characters, with each option name limited to 255 characters.
     * **Calendar** : A date and time field. The default format is `DD/MM/YYYY HH:MM:SS`.
  6. Click **Save**.




## Use case: Use custom fields to enhance phishing resistance

This use case outlines the steps to define three custom fields: a radio button, a single-select list, and a calendar, and how to add them to the **Custom Field Form** widget. These fields enrich the default alert view with additional information for phishing alerts.

### Define the False Positive custom field

  1. For **Scope** , select **Alert**.
  2. In the **Name** field, enter `False Positive`.
  3. In the **Type** list, select **Radio Button**.
  4. In the **Options** field, enter `True Positive` (then press **Enter**), and then enter `False Positive` (then press **Enter**).
  5. Click **Save**.



### Define the User Action custom field

  1. Click **Add** to create another new custom field.
  2. For **Scope** , select **Alert**.
  3. In the **Name** field, enter **User Action**.
  4. In the **Type** list, select **Single Select**.
  5. In the **Options** field, enter `Clicked` (then press **Enter**), `Reported` (then press **Enter**), and then `Ignored` (then press **Enter**).
  6. Click **Save**.



### Define the Report Time custom field

  1. Click **Add** to create another new custom field.
  2. For **Scope** , select **Alert**.
  3. In the **Name** field, enter `Report Time`.
  4. In the **Type** list, select **Calendar**.
  5. Click **Save**.



### Add custom fields to the alert-level widget

After defining custom fields, add them to the **Custom Fields Form** widget. Each widget can hold up to fifty custom fields. The following steps show how to add the three custom fields you created previously to the **Custom Fields Form** widget to enrich the default alert view.

  1. Go to **SOAR Settings** > **Case Data** > **Views** > **Default Alert View**. The **Default Alert View** opens with the available widgets.
  2. On the **General** tab, drag the **Custom Fields Form** widget to the **Default Alert View**.
  3. In the **Custom Fields Form** widget, click  **Settings** **Configuration** to open its settings.
  4. In the **Widget Title** field, enter `True or False Positive Alert`.
  5. Select **Manage Custom Fields**.
  6. Select the **False Positive** , **User Action** , and **Report Time** checkboxes, and then click **Save**. The system adds these custom fields to the **Custom Fields Form** widget.
  7. Click the **Mandatory** toggle.
  8. Select **Save** to save the configuration and close the window.
  9. Click **Save View**.



### Use the Custom Fields Form widget

After you add custom fields to the **Custom Fields Form** widget, it appears in the **Overview** tab of cases and alerts. Analysts can then enter the required information directly. Building on the previous example, follow these steps to use the widget:

  1. On the **Alert Overview** tab, select the **Custom Fields** widget, and click edit **Edit**.
  2. Fill in the relevant information for the three custom fields: 
     * **False Positive** : Select the radio button to indicate if the alert is a `true` or `false` positive.
     * **User Action** : Select **Clicked** , **Reported** , or **Ignored**.
     * **Report Time** : Select the date the alert was reported.
  3. Click **Save**.



## Use custom fields in playbooks

You can use the custom fields you define on this page as part of playbook actions and placeholders. For more information about playbook actions, see [Integrate Siemplify with Google SecOps](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify).

### Placeholders for custom fields

Custom fields are available under the **Custom Fields** placeholder category. Use the following format for these placeholders:

  * `\[AlertCustom.{custom field name}\]`
  * `\[CaseCustom.{custom field name}\]`



## Use custom fields in advanced reports

Custom fields created for cases can be used in advanced reports to gain deeper insights from your data.

**Note:** Advanced reports support only custom fields that have a **Case** scope.

### Create custom fields for single-select values in Looker 

To reference a single-select custom field (for example, `"Country"`) in a Looker report, use the following LookML formula as a calculated field:
    
    
        if(
          contains(${vw_cases_custom_values.custom_field_json},"\"Country\":"),
          replace(
          replace(
          replace(
            if(position(
              replace(
                ${vw_cases_custom_values.custom_field_json},
                substring(
                  ${vw_cases_custom_values.custom_field_json},
                  0,
                  ( position(
                    ${vw_cases_custom_values.custom_field_json},
                    "\"Country\":")
                    +
                    length("\"Country\":")
                  )
                ),
                ""
              ),
              "\","
            )>0,
    
            substring(
              replace(
                ${vw_cases_custom_values.custom_field_json},
                substring(
                  ${vw_cases_custom_values.custom_field_json},
                  0,
                  ( position(
                    ${vw_cases_custom_values.custom_field_json},
                    "\"Country\":")
                    +
                    length("\"Country\":")
                  )
                ),
                ""
              ),
              0,
              position(
                replace(
                  ${vw_cases_custom_values.custom_field_json},
                  substring(
                    ${vw_cases_custom_values.custom_field_json},
                    0,
                    ( position(
                      ${vw_cases_custom_values.custom_field_json},
                      "\"Country\":")
                      +
                      length("\"Country\":")
                    )
                  ),
                  ""
                ),
                "\","
              )
            ),
            replace(
              ${vw_cases_custom_values.custom_field_json},
              substring(
                ${vw_cases_custom_values.custom_field_json},
                0,
                ( position(
                  ${vw_cases_custom_values.custom_field_json},
                  "\"Country\":")
                  +
                  length("\"Country\":")
                )
              ),
              ""
            )),
            " \"",
            ""
          ),
          "\"",
          ""
        ),
        "}",""),
        null
        )
        

**Tip:** To use this formula for a different single-select custom field, replace all instances of `"Country"` with the exact name of your custom field. 

### Create custom fields for multi-select values in Looker 

To reference a multi-select custom field (for example, `"Department"`) in a Looker report, use the following LookML formula as a calculated field:
    
    
        if(contains(${vw_cases_custom_values.custom_field_json},"\"Department\""),
    
        substring(
    
        replace(
        replace(
    
        substring(${vw_cases_custom_values.custom_field_json},
        position(
        ${vw_cases_custom_values.custom_field_json},
        "\"Department\""),length(${vw_cases_custom_values.custom_field_json}))
    
    
        ,"\", \"Department\":\"",","),
    
        "\"Department\":\"","")
    
    
        ,0, position(replace(
        replace(
    
        substring(${vw_cases_custom_values.custom_field_json},
        position(
        ${vw_cases_custom_values.custom_field_json},
        "\"Department\""),length(${vw_cases_custom_values.custom_field_json}))
    
    
        ,"\", \"Department\":\"",","),
    
        "\"Department\":\"",""),"\"")-1)
    
        , null)
        

**Tip:** To use this formula for a different multi-select custom field, replace all instances of ``"Department"`` with the exact name of your custom field. 

### Filter custom fields in Looker 

To effectively filter custom fields in Looker, the method you use depends on whether you are working with a Look or a dashboard.

#### Filtering in a Look

To filter both single-select and multi-select custom fields in a Look, you can directly use the custom dimension field created with the preceding formulas.

#### Filtering on dashboards

To filter custom fields on dashboards, you must reference the underlying JSON value from **Explore** and use the appropriate values in the filter, as follows:

  * **Single-select fields:** For example, to filter for cases where the **Country** custom field is `China`, use the filter condition: `%"Country": "China"%` (where the exact syntax might vary slightly depending on the Looker version).
  * **Multi-select fields:** To filter multi-select fields with dashboards, reference and use the JSON value and appropriate syntax, which can vary based on your filtering needs (for example, matching any or all selected values).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
