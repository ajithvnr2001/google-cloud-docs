---
url: https://docs.cloud.google.com/data-studio/visualize-bigquery-geography-polygons/
title: Visualize BigQuery GEOGRAPHY polygons with Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:21.633664+00:00
---

# Visualize BigQuery GEOGRAPHY polygons with Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/visualize-bigquery-geography-polygons/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Visualize BigQuery GEOGRAPHY polygons with Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

![](https://docs.cloud.google.com/static/data-studio/images/bluestopwatchtimersessionicon-2015-09-11.png)

This tutorial is intended for people who want to visualize `GEOGRAPHY` data from BigQuery using Data Studio. To complete this tutorial, you'll need a BigQuery billing project. You don't need to know how to write SQL, and you can use the public dataset.

## Goals

In this tutorial, you'll create a report that shows the affordability of rental properties in Washington state. You'll use a Google Map to visualize `GEOGRAPHY` data coming from a public BigQuery dataset.

![A Google map displays red BigQuery geography polygons that represent rent affordability by county in Washington state.](https://docs.cloud.google.com/static/data-studio/images/eap-doc12-2021-03-22.png)

In this tutorial, you'll accomplish the following:

  * Create a new blank report
  * Add a Google Map to the report
  * Configure the map
  * Style the map
  * Interact with the map
  * Change the tooltip
  * Add more style to the map



### Before you begin

If you don't already have a BigQuery billing project set up, you can [sign up for free](https://cloud.google.com/bigquery/).

## Create a new blank report

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** and then select **Report**.
  3. In the **Add data to report** panel, choose **BigQuery**.

![](https://docs.cloud.google.com/static/data-studio/images/select-bq.png)

  4. In the left navigation, choose **CUSTOM QUERY**.

  5. Select or enter your billing project ID.

  6. Under **Enter Custom Query** , paste the following SQL query:
         
         select
                 ct.state_fips_code,
                 ct.county_fips_code,
                 c.county_name,
                 ct.tract_ce,
                 ct.geo_id,
                 ct.tract_name,
                 ct.lsad_name,
                 ct.internal_point_lat,
                 ct.internal_point_lon,
                 ct.internal_point_geo,
                 ct.tract_geom,
                 acs.total_pop,
                 acs.households,
                 acs.male_pop,
                 acs.female_pop,
                 acs.median_age,
                 acs.median_income,
                 acs.income_per_capita,
                 acs.gini_index,
                 acs.owner_occupied_housing_units_median_value,
                 acs.median_rent,
                 acs.percent_income_spent_on_rent,
             from `bigquery-public-data.geo_census_tracts.census_tracts_washington` ct
             left join `bigquery-public-data.geo_us_boundaries.counties` c
                 on (ct.state_fips_code || ct.county_fips_code) = c.geo_id
             left join `bigquery-public-data.census_bureau_acs.censustract_2018_5yr` acs
                 on ct.geo_id = acs.geo_id
         

**Note:** This query retrieves data from BigQuery Public Datasets about US census tracts in Washington state. A census tract is a relatively small subdivision of a county. The query joins the geospatial data about the census tract boundaries with census statistics, such as population, age, income, and housing costs.
  7. Click **Add** to add this data to the report.




## Add a Google Map to the report

  1. Delete the table on the report page.
  2. Click **Add a chart.**
  3. In the **Google Maps** section, click **Filled map.**



## Configure the map

![A user selects geo_id for the Location field and tract_geom for the Geospatial field in the Data tab of a Google Maps chart Properties panel.](https://docs.cloud.google.com/static/data-studio/images/eap-doc3-2021-03-22.png)

The map won't appear yet. You'll need to add the field that uniquely identifies each location first.

  1. In the **Location** section, click **Invalid dimension** , and then choose **geo_id**. 
     1. This field uniquely identifies each census tract.
  2. In the **Geospatial** **field** section, click **Add metric** , and then choose **tract_geom**. 
     1. This field contains the BigQuery `GEOGRAPHY` data that defines the polygons that you want to display.



The map should look like this:

![A Google map with blue geography polygons representing rent affordability in Washington state by county displays polygons only for a few counties.](https://docs.cloud.google.com/static/data-studio/images/eap-doc13-2021-03-22.png)

> **Why is the map missing polygons?** A Google Map in Data Studio plots 100K points (polygon vertices) by default, but the **tract_geom** column contains 911,364 points. You can increase the number of points (up to a maximum of 1 million) or, to reduce the number of points, you can add a filter to focus on a specific area. In the **STYLE** tab of the chart properties panel, in the **Filled Area Layer** section, set the **Max number of polygon vertices** to **1,000,000**. ![](https://docs.cloud.google.com/static/data-studio/images/max-polygon-vertices-2024-06-25.png)

### Add a county filter

  1. In the toolbar, click **Add a control**.
  2. Select **Drop-down list**.
  3. Set the **Control** field to **county_name** , and, for **Default selection** , enter **King**.



![A user selects Drop-down list from the Add a control menu and selects county_name as the Control field with King as the default selection in the Setup tab of the Properties panel.](https://docs.cloud.google.com/static/data-studio/images/filter-by-countyname-2021-03-29.png)

Now you should see all polygons for King County, which contains Seattle:

![A Google Maps chart with blue geography polygons representing rent affordability in Washington state by county filtered to display King County data.](https://docs.cloud.google.com/static/data-studio/images/eap-doc18-2021-03-22.png)

## Style the map

The map's default color metric is **Record Count**. You can also choose a different metric.

In the **Color metric** section, choose **percent_income_spent_on_rent**.

## Interact with the map

Depending on the options that you turned on, you can zoom and pan around and notice census tracts where people spend nearly half their income on rent, such as the University District in Seattle:

## Change the tooltip

As you mouse over the map, you'll notice that the tooltip shows the `geo_id`, which isn't particularly meaningful in this context:

![A tooltip on the Washington state rent Google Maps chart with a geo_id tooltip dimension displays the data point details 53033005301 percent_income_spent_on_rent: 51.](https://docs.cloud.google.com/static/data-studio/images/eap-doc21-2021-03-22.png)

You can provide viewers with a more useful tooltip by changing the **Tooltip** dimension.

  1. In the report, click **Edit**.
  2. Select the map.
  3. In the **Tooltip** section of the properties panel, choose **lsad_name**. 
     1. This field contains the human-readable census tract name:



![The Setup tab on the Properties panel displays geo_id as the Location field, tract_geom as the Geospatial field, lsad_name as the Tooltip field, and percent_income_spent_on_rent as the Color metric.](https://docs.cloud.google.com/static/data-studio/images/geography-fields-2021-03-22.png)

## Add more style to the map

You can customize the appearance of the map in the **STYLE** tab. For example, you could increase the fill opacity to 80% and change the color gradient from blue to red.

![Filled Area Layer section options and Colors section options on the Filled Map Style tab.](https://docs.cloud.google.com/static/data-studio/images/map-colors-2021-03-22.png)

![The final Google map with red gradient geography polygons representing rent affordability in Washington state with the tooltip text Census Tract 295.02 percent_income_spent_on_rent: 47.5 displayed for a data point.](https://docs.cloud.google.com/static/data-studio/images/final-map-2021-03-22.png)

## Congratulations

You've created a Google Map in Data Studio that visualizes BigQuery `GEOGRAPHY` data.

## Related resources

  * [Connect to Google BigQuery](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery)
  * [BigQuery Public Datasets](https://console.cloud.google.com/marketplace/browse?q=geo&filter=solution-type:dataset) (several datasets with geographic polygon data)
  * [Google Maps reference](https://docs.cloud.google.com/data-studio/google-maps-reference)
  * [BigQuery geography functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions)
  * [Visualize BigQuery Places Insights data dynamically with Data Studio](https://developers.google.com/maps/architecture/places-insights-looker-studio)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
