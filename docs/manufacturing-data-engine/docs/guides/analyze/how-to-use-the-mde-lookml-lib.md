---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/analyze/how-to-use-the-mde-lookml-lib/
title: Use the LookML Library \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:37.858989+00:00
---

# Use the LookML Library  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/analyze/how-to-use-the-mde-lookml-lib/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the LookML Library

The LookML Library for MDE provides abstract core files, and packaged views, explores and dashboards to help you get started with building your own LookML models on top of the MDE data in BigQuery.

## Before you begin

To complete this guide, you need the following prerequisites:

  * You configured a new Looker project using the _MDE Project Template_ as described in the [setup guide](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/analyze/how-to-set-up-a-new-mde-Looker-project).
  * You have an active MDE deployment.
  * **Optional**. You applied the default [MDE configuration package](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/guide#apply-the-default-configuration-packages). While you can use the _MDE LookML Library_ to create custom views, the _default_ LookML package requires the _default_ MDE configuration package is applied.



## Exploring library contents

After the project is allowed, you can explore the contents of the library under the `imported_projects/mde_lookml_lib` directory in the Looker development console. The library provides content in two directories:

  * `mde_abstract_core`
  * `mde_packages`



### Abstract core directory

The `mde_abstract_core` directory provides base views that you can use to model MDE metadata buckets as dimensions and MDE record tables as fact tables in Looker. The base views save you from needing define the shared fields across these views.

The library provides a `dim_base.view` view for building dimensions, which you can find in `imported_projects/mde_lookml_lib/mde_abstract_core/views/dimension/dim_base.view.lkml`. The following example shows how you can extend the base view to define a dimension called `device`:
    
    
    include: "//mde_lookml_lib/mde_abstract_core/views/dimension/*.view"
    
    view: dim_source {
    
       derived_table: {
          sql: SELECT * FROM `mde_dimension.metadata-store` where bucket_number = BUCKET_NUMBER ;;
       }
    
       view_label: "DIM - Device"
       extends: [ dim_base ]
    
       dimension: device_name {
          type: string
          sql: JSON_VALUE(${TABLE}.instance,"$.device_name") ;;
       }
    
    }
    

And, similarly, the library provides base views per MDE archetype for modeling record tables in BigQuery as fact tables. You can find the base views under `imported_projects/mde_lookml_lib/mde_abstract_core/views/fact/`. You can extend the archetype base views to define custom fact views in Looker. The following example shows how you can define a fact view called `sensor_readings`:
    
    
    include: "//mde_lookml_lib/mde_abstract_core/views/fact/fct_numeric_archetype.view"
    
    view: fct_sensor_readings {
       extends: [ fct_numeric_archetype ]
       label: "FCT - Sensor Readings"
       sql_table_name: `mde_data.sensor-readings` ;;
    }
    
    

### Packages

The `mde_packages` directory contains prebuilt LookML packages for MDE. These packages provide use-case specific explores, views and dashboards to get you started quickly.

The _default_ Looker configuration package works in conjunction with the _default_ MDE configuration package. For more information, see the [Default configuration package guide](https://docs.cloud.google.com/manufacturing-data-engine/docs/resources/default-configuration-package). The default Looker configuration package provides a fact table per record table linked to an MDE type, as well tag and source dimensions, which correspond to the tag and source metadata buckets in MDE, respectively.

If you used the MDE Project Template to [bootstrap](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/analyze/how-to-set-up-a-new-mde-looker-project) a new MDE project, the provided Looker model automatically imports the views and explores from the default package:
    
    
    connection: "@{looker_connection}"
    
    ########## DEFAULT MDE EXPLORES ##########
    include: "//mde_lookml_lib/mde_packages/default/explores/default.explore.lkml"
    
    ############ CUSTOM VIEWS ################
    include: "/views/dimension/*.view"
    include: "/views/fact/*.view"
    

Once your project is set up, you can use the default default explores in Looker to analyze data.

You can also use other configuration packages included in the library. See the following section for further instructions and prerequisites to use these packages in the library.

## Extend views provided by the configuration packages in the library

You can extend the fact and dimension views included in the library by using the [extends](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends#:%7E:text=To%20extend%20a%20LookML%20object,versions%20of%20the%20LookML%20object.) syntax. For example, in your project model file you can extend the `dim_tag` by defining additional dimension fields on the deviceMetadata object, as the following script shows:
    
    
    view: +dim_tag {
    dimension: device_type {
    type: string
    sql: JSON_VALUE(${TABLE}.instance,"$.deviceMetadata.deviceType") ;;
    }
    dimension: location {
    type: string
    sql: JSON_VALUE(${TABLE}.instance,"$.deviceMetadata.location") ;;
    }
    }
    

## Dashboards access is defined in the _default_ configuration package

The LookML model defined in the _MDE Project Template_ imports all the dashboards from the default package in _MDE LookML Library_. To access any of these dashboards, open the following link:

`https://LOOK_HOST/dashboards/mde::DASHBOARD_ID`

Replace the following:

  * `LOOK_HOST` with the hostname of your Looker instance.
  * `DASHBOARD_ID` with the ID of the dashboard you want to open. You can look up the dashboard ID, by opening the relevant .dashboard file in the `imported_projects/mde_lookml_lib/mde_packages/default/dashboards/` directory and copying the value of the `dashboard` property.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
