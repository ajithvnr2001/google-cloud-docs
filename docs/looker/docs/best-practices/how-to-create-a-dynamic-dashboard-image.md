---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-dynamic-dashboard-image/
title: Create a dynamic dashboard image with Liquid and HTML \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:36.072121+00:00
---

# Create a dynamic dashboard image with Liquid and HTML  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-dynamic-dashboard-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Create a dynamic dashboard image with Liquid and HTML Stay organized with collections  Save and categorize content based on your preferences. 

You can add images to Looker dashboards by hard-coding an image URL in a Markdown [text tile](https://docs.cloud.google.com/looker/docs/using-markdown-in-text-tiles#images). However, images in text tiles are static and will not update based on results. What if you want a dashboard image to dynamically change based on a user-selected filter value? 

This Best Practices page demonstrates how to achieve a dynamic dashboard image using [Liquid](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) and the [`html` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-html). 

## The solution

The following solution is based on an e-commerce data set that includes a field called `users.state`, representing the states in a hypothetical ecommerce data set: 
    
    
    dimension: state {
      type: string
      sql: ${TABLE}.state ;;
    }
    

Say that you want to display the image of a state's flag on a dashboard that will update based on the state by which a user chooses to filter the dashboard results. 

There are three steps that you need to complete to create the dynamic dashboard image: 

  1. Create an image dimension in LookML. 
  2. Create a dynamic image dashboard tile. 
  3. Add dashboard filters and final touches. 



### Step 1: Create an image dimension in LookML

To create an image dimension in LookML: 

  1. First, navigate to the project and view file containing the dimension to which you would like to add images. Then, create a new dimension based on that field, specifically for the use of displaying the images. 
  2. Add an `html` parameter for defining a Liquid [`{% if %}` conditional statement](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#basic_examples) with the [`value`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#liquid_variable_definitions) variable, for each value for which you want to display an image. 

For example, the following `state_flag_image` dimension establishes a condition for displaying the specified images (with `html <img> `tags) when the value of `state` is `"California"`, `"New York"`, `"Colorado"`, or `"Illinois"`. For all other states, you can display a "no image available" icon: 
         
         dimension: state_flag_image {
                   type: string
                   sql: ${state} ;;
                   html:
                       {% if state._value == "California" %}
                       <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg" height="170" width="255">
                       {% elsif state._value == "New York" %}
                       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_New_York.svg/1200px-Flag_of_New_York.svg.png" height="170" width="255">
                       {% elsif state._value == "Colorado" %}
                       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Flag_of_Colorado.svg/255px-Flag_of_Colorado.svg.png" height="170" width="255">
                       {% elsif state._value == "Illinois"%}
                       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Illinois.svg/1200px-Flag_of_Illinois.svg.png" height="170" width="255">
                       {% else %}
                       <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png" height="170" width="170">
                       {% endif %} ;;
               }
             

  3. Create a value condition for each value for which you would like to display an image. Alternatively, you can create a dynamic image field using the `value` Liquid variable, as described in the [How to add images to visualizations](https://discuss.google.dev/t/how-to-add-images-to-visualizations/119279) Community post. 



Next, you can create a dashboard tile for the image dimension. 

### Step 2: Create a dynamic image dashboard tile

Now that the image dimension (`state_flag_image`) has been created, you can build an Explore that will become the dynamic image dashboard tile. 

Build your Explore with the following criteria:

  * Add a filter for the original dimension (in this case, `state`). Set the filter for any value. This will cause the "no image available" image to be displayed initially, as no specific filter value is selected. This filter value will update according to what the user selects for the dashboard filter. 
  * Select the image dimension (in this case, `state_flag_image`) and any other dimensions that may be necessary to the query that determines the image (for example, if you want to factor in a date, you can include date, etc.). 
  * Change the [row limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#limiting_data) to one row. 
  * Change the visualization type to a [single value visualization](https://docs.cloud.google.com/looker/docs/single-value-options) and [hide](https://docs.cloud.google.com/looker/docs/creating-visualizations#specifying_lookml_fields_to_include_in_the_visualization) any other columns except the image dimension (`state_flag_image`). 



Your Explore will initially display the "no image available" image in the single value visualization rendered in the **Visualization** panel. The display image will change based on the filter value the user selects on the final dashboard: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-dynamic-dashboard-image-explore-2210.png)

Save the Explore to a dashboard as a [tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore). 

### Step 3: Add dashboard filters and final touches

Now you need to add dashboard filters to the dashboard. The filters on the dashboard will update the filter in the Explore to change the image displayed based on user selection. 

From the dashboard's edit mode, [create the filter](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding_dashboard_filters): 

  * Open the [**Add filter window**](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#the_add_filter_window)
  * Select the field to filter by. The filter field should be the dimension on which the image dimension is based. In the case of this example, the field for the filter will be **state**. 
  * Select the image tile from Step 2 on the **Tiles to Update** tab. 
  * Select the original dimension (**state** in this case) in the inline **Field to Filter** drop-down menu. 
Select other tiles to update as desired. 
  * [Customize](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#customizing_filter_configuration) the filter as desired. If you select the **Advanced** [control option](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#using_advanced_controls), make sure to deselect the **Allow multiple filter values** option, which is automatically enabled for the **Advanced** control option. 



Now, the image tile will update with the user filter selection. 

When a user chooses to filter by "California", the dashboard will display the state flag and data for the state of California: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-dynamic-dashboard-image-dashboard-1-2210.png)

When a user chooses to filter by "Colorado", the dashboard will display the state flag and data for the state of Colorado: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-dynamic-dashboard-image-dashboard-2-2210.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
