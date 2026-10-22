---
url: https://docs.cloud.google.com/looker/docs/types-of-dashboards/
title: Comparing user-defined and LookML dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:50.903193+00:00
---

# Comparing user-defined and LookML dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/types-of-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Comparing user-defined and LookML dashboards Stay organized with collections  Save and categorize content based on your preferences. 

A Looker dashboard is a collection of queries displayed as visualizations on a screen. Users can [alter filters](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) on dashboards, [apply alerts](https://docs.cloud.google.com/looker/docs/creating-alerts) to tiles, set up [dashboard delivery schedules](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards), and [download](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_dashboard) a dashboard's data, among other things.

There are two types of Looker dashboards: [user-defined dashboards](https://docs.cloud.google.com/looker/docs/dashboards) and [LookML dashboards](https://docs.cloud.google.com/looker/docs/reference/lookml-dashboard-overview).

Each type of dashboard has different benefits and constraints:

Characteristic | User-Defined Dashboard | LookML Dashboard  
---|---|---  
Generally created and edited by | Business users and Looker developers. | A select group of LookML developers.  
Defined | By adding query tiles, Look-linked tiles, or text in the user interface; arranging them using drag-and-drop operations; and adding and formatting dashboard filters and other options (as described on the [Creating user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards) documentation page). | Written and edited in a YAML-based dashboard file, as described in the [Creating a LookML dashboard file](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#creating_a_lookml_dashboard_file) section of the [Building LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards) documentation page.  
Updated | When the dashboard is edited or the corresponding saved Looks are updated. | When the LookML file for the dashboard is edited.  
Stored | In a user's personal folder or in a shared folder for easy collaboration across a wider group of users. | As version-controlled files that are associated with the project in a Git repository. By default, LookML dashboards are accessible for viewing in the [**LookML dashboards**](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#lookml_dashboards_folder) folder located in the [**All folders**](https://docs.cloud.google.com/looker/docs/finding-content#top-level_folders) top-level folder. They can also be [moved to other folders](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#moving_lookml_dashboards_outside_of_the_lookml_dashboards_folder) as desired. LookML dashboards are not shown in the **Recently Viewed** tab of the homepage or on the **Recently viewed** page.  
Convertible | To LookML dashboards, as described in the [Getting dashboard LookML from a dashboard](https://docs.cloud.google.com/looker/docs/viewing-dashboards#getting_dashboard_lookml_from_a_dashboard) section of the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) documentation page. | To user-defined dashboards, as explained on the [Converting from LookML to user-defined dashboards](https://docs.cloud.google.com/looker/docs/converting-lookml-to-user-defined-dashboard) documentation page.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
