---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-change-the-model-or-explore-of-a-look/
title: Changing the model or Explore of a Look or dashboard \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:35.077357+00:00
---

# Changing the model or Explore of a Look or dashboard  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-change-the-model-or-explore-of-a-look/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Changing the model or Explore of a Look or dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Occasionally, you may want to change the model or source Explore of a Look or dashboard. For example, you have a Look or dashboard that is based on LookML from model A. You also have a second model — model B. You want to change the model reference of a Look or dashboard to model B instead of model A. This page addresses how to change the source model or Explore for a Look or dashboard. 

There are multiple solutions, depending on the use case:

  * For a single Look: 
    * Edit the Look's expanded URL. 
    * Overwrite the Look with another Look.
  * For one or more dashboards, create a LookML copy. 
  * For multiple Looks or dashboards: 
    * Use the Looker API. 
    * Use the Looker Content Validator. 



## Edit the Look's expanded URL

For a one-off Look, you can use the [expanded URL](https://docs.cloud.google.com/looker/docs/sharing-urls#expanded_url) from the Look's underlying Explore to change the model name in the URL. 

  1. From the Look, select the **Explore from Here** link to open the Look's query in an Explore. 
  2. Select **Share** from the Explore's gear menu to open the **Share URLs** menu. 
  3. Copy the URL from the **Expanded URL** option.
  4. Change the model name in the expanded URL. The model name comes right after the instance name and the `/explore` part of the URL. The URL takes the following form:

` https://instance_name.looker.com/explore/MODEL_NAME/EXPLORE_NAME?fields=... `

In this example, the model name is `lauren_ecommerce`: ![Expanded URL with /explore/lauren_ecommerce/order_items?fields=orders.created_month,orders.count after the instance name.](https://docs.cloud.google.com/static/looker/docs/images/hc-change-model-explore-expanded-url-2210.png)
  5. Paste the new Explore URL in a browser to verify that it works with the updated model name. 
  6. [Save the Explore as a new Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore), or overwrite your existing Look. 



## Overwrite a Look with another Look

You can overwrite a Look with another Look that is based on the selected model or Explore. 

  1. [Build an Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores) that is based on the selected model or Explore. 
  2. [Save the Explore as a Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore) with the same name in the same folder as your existing Look, which will overwrite your existing Look. 



## Create LookML copies of dashboards

You can convert one or more dashboards to a LookML dashboard and update the dashboard's model in the LookML: 

  1. For each dashboard, [create a LookML copy of the dashboard](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#create_a_lookml_copy_of_a_user-defined_dashboard) and save it in your LookML project. (If your dashboards are already LookML dashboards, you can skip this step.) 
  2. In your LookML project, use the Looker IDE's [search and replace function](https://docs.cloud.google.com/looker/docs/looker-ide#finding_and_replacing_text_in_your_project) to find instances of `model:`, and then update the value to a different model name. 
  3. You can leave the updated dashboards as LookML dashboards, or you can [convert them to user-defined dashboards](https://docs.cloud.google.com/looker/docs/converting-lookml-to-user-defined-dashboard). 



## Use the Looker API

You can use the Looker API to update the model for multiple dashboards: 

  1. Use the [`dashboard_elements`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element) API endpoint to get all the dashboard elements. The response will provide the query IDs. 
  2. If any of the dashboard tiles are [Look-linked tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles), use the [`looks`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/look) endpoint to find the query ID of the underlying Look. 
  3. For each of the query IDs: 
     1. Call the [`query`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/query) endpoint to get the response body of the query. 
     2. Copy the `query` response body. 
     3. Update the `model` key's value to your new model. 
     4. Use the [`create_query`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/create_query) endpoint to create a new query, passing in the edited body. 
  4. For the dashboard, change the query ID for each of the elements by using the [`update_dashboard_element`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard_element) endpoint, passing in the edited body. 



## Use the Looker Content Validator

The [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) is a tool that checks Looks and dashboards for errors, and it also has a [ Find & Replace in All Content](https://docs.cloud.google.com/looker/docs/content-validation#using_the_content_validator_to_find_and_replace) feature, which you can use to change the underlying model or Explore for all Looks or dashboard tiles. 

> The **Find & Replace in All Content** feature changes _all_ Looks and dashboards on the Looker instance. To apply a change to only a few Looks or dashboard tiles, you can make a breaking change, as described in the following steps. 

If you don't want to change the model or Explore reference for all content across an instance, but do want to change the reference for more than one Look or dashboard tile at a time, you can use the Content Validator to replace the references for a handful of Looks or dashboard tiles all at once: 

  1. Enable [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode) to ensure that no users are impacted by the changes made in the following steps. 
  2. Intentionally "break" the existing model by renaming the model file in the Looker IDE to another name that you know does not exist, such as `zzz`. This will cause every Look and dashboard that uses the original model to break. 
  3. Select **Content Validator** in the **Develop** menu to open the Content Validator. 
  4. Select **Validate** to [run the Content Validator](https://docs.cloud.google.com/looker/docs/content-validation#running_the_content_validator). 
  5. In the Content Validator results, select the **Content** button to [group the results by content](https://docs.cloud.google.com/looker/docs/content-validation#group_by_content). 
  6. Find the Looks or dashboard tiles for which you want to change the model reference. 
  7. Select the **Replace** button for each individual Look or dashboard to [replace the "broken" model name with the new model name you want to use](https://docs.cloud.google.com/looker/docs/content-validation#replacing_names_for_fields,_views,_explores,_and_models). 
  8. Check that the Looks or dashboard tiles work as expected now that they point to the new model. 
  9. Finally, go back to your project and rename the model file in the Looker IDE back to its original name and run the Content Validator again to verify that all validation errors are cleared. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
