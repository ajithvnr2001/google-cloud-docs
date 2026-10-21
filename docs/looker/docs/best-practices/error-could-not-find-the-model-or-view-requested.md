---
url: https://docs.cloud.google.com/looker/docs/best-practices/error-could-not-find-the-model-or-view-requested/
title: Error: Could not find the model or view requested \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:41.815003+00:00
---

# Error: Could not find the model or view requested  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/error-could-not-find-the-model-or-view-requested/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Error: Could not find the model or view requested Stay organized with collections  Save and categorize content based on your preferences. 

## The error

You may see the following error on an Explore, a Look, or a dashboard: 
    
    
    Could not find the model or view requested.
    

## Common causes

Some common causes of this error include the following: 

  * **Typo in the URL:** If you manually created an Explore URL, check the model and Explore name in the URL to make sure that they are correct. 
  * **Explore or model name has changed:** Each Look or dashboard query is based on a [model](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) and an [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores). If the model name or Explore name changes, the Look or dashboard query will still reference the old name until you update it with the new name. For example, if the name of an Explore is changed from `old-name` to `new-name`, any associated Looks or dashboard queries will still try to use the `old-name` Explore until you update them. 



## Troubleshooting

There are multiple ways to resolve this error, but you can resolve most instances just by replacing the incorrect model or Explore name with a valid name. Use the following methods to update either a single query or all Looks and dashboards on your Looker instance: 

  * Change the URL of a single query
  * Use the Content Validator



### Change the URL of a single query

If you know that an Explore name or a model name has been changed, you can fix individual Looks and dashboards by using the [expanded URL](https://docs.cloud.google.com/looker/docs/sharing-urls#expanded_url). The expanded URL contains the model name, the Explore name, and the field names. You can take advantage of this function to change the Explore or model name of the query. 

![](https://docs.cloud.google.com/static/looker/docs/images/explore-expanded-url-2210.png)

  1. Select **Explore from here** from the Look or dashboard query. 
  2. Select the [**Explore actions** gear menu](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu) next to **Run** and **Edit** , and then select **Share**. 
  3. Copy the expanded URL and paste it somewhere else, such as into a document or your browser's address bar. (If you paste the URL into your browser's address bar, do not press Enter yet; if you do, the expanded URL will be turned into a shortened URL.) 
  4. Modify the URL text to change the name of the Explore. The URL takes the following form: 
         
         https://instance_name.looker.com/explore/MODEL_NAME/EXPLORE_NAME?fields=...

  5. If necessary, copy and paste the expanded URL into your browser, and press Enter or Return to navigate to the URL. 
  6. Save the Explore as a Look or dashboard query.




### Use the Content Validator

The [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) has a [find-and-replace](https://docs.cloud.google.com/looker/docs/content-validation#using_the_content_validator_to_find_and_replace) function. You can use this to replace the Explore name across all Looks. This will change _every_ Look and dashboard query that uses `old-name`, however, so take this step with caution. 

## I'm still seeing this error. Now what?

If you've tried the previous steps and continue to see the error, check with a Looker admin at your company to make sure that the requested model and Explore exist on your Looker instance. If you're still stuck, [contact Looker support](https://console.cloud.google.com/support/) for further troubleshooting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
