---
url: https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization/
title: visualization \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.241775+00:00
---

# visualization  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  visualization Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    visualization: {
      id: "unique-id" 
      label: "Visualization Label" 
      url: "visualization_url" 
      sri_hash: "SRI hash" 
      dependencies: ["dependency_url_1","dependency_url_2"]
      file: "visualization_file_path" 
    }
    

Hierarchy [Manifest File](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) `visualization` |  Default Value None Special Rules The `visualization` must have either a `url` or a `file` parameter, but not both   
---|---  
  
## Definition

The `visualization` parameter adds a custom visualization to your LookML project that users can access from the **Visualization** tab in the project's Explores. The custom visualization must be defined in a JavaScript file, which can be included in your LookML project files, or hosted elsewhere.

The `visualization` parameter has the following subparameters:

Parameter | Description  
---|---  
`id` | Specifies a unique identifier for the visualization that is displayed in the [**Visualizations** page of Looker's **Admin** menu](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations).   
`label` | Provides the label for the visualization that is displayed in the [**Visualization** tab](https://docs.cloud.google.com/looker/docs/creating-visualizations#choosing_a_visualization_type) of your project's Explores and in the [**Visualizations** page of Looker's **Admin** menu](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations).   
`url` | The `url` parameter provides the URL to the visualization's JavaScript file, if the file is stored on a server outside the Looker instance. Instead of using the `url` parameter, you can [drag and drop the file into the Looker IDE](https://docs.cloud.google.com/looker/docs/other-project-files#adding_data_files) and then use the `file` parameter to point to the file. **NOTE** : The application must have either a `url` parameter or a `file` parameter, but not both.   
`sri_hash` | The SRI hash is used only when the visualization's JavaScript file is specified with the `url` parameter. If the site hosting your custom visualization code uses a [subresource integrity (SRI) hash](https://en.wikipedia.org/wiki/Subresource_Integrity) for verification purposes, enter the SRI hash in the `sri_hash` field.   
`dependencies` | Provides a comma-separated list of dependency URLs required to load the visualization.   
`file` | Specifies the path to a JavaScript file (with a `.js` extension) that defines the visualization. The path is relative to the project root. The example in the next column points to the `calendar-heatmap.js` file in the `visualizations` directory of the LookML project. **NOTE** : The application must have either a `url` parameter or a `file` parameter, but not both.   
  
## Example: Adding a custom visualization URL to your LookML project

One option for adding a custom visualization to your LookML project is to use the URL of a custom visualization file. For example, adding this LookML to a project's manifest file adds a multiple-value CDN custom visualization to the Looker project. This visualization is defined in a JavaScript file located on Looker's Marketplace:
    
    
    visualization: {
      id: "spider-marketplace-dev"
      label: "Spider Viz"
      url: "https://marketplace-api.looker.com/viz-dist/spider.js"
      sri_hash: "oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
      dependencies: ["https://code.jquery.com/jquery-2.2.4.min.js","https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.1/underscore-min.js","https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js","https://cdnjs.cloudflare.com/ajax/libs/d3-legend/1.13.0/d3-legend.min.js"]
    }
    
    

Once you [commit](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes) your changes and [deploy them to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production), Looker displays the name of the custom visualization as an option in the [**Visualization** tab](https://docs.cloud.google.com/looker/docs/creating-visualizations#choosing_a_visualization_type) of your project's Explores.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-cust-viz-url-718.png)

The visualization will also be listed on the **Visualizations** page in the **Platform** section of Looker's **Admin** menu; see the [Admin settings - Visualizations](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations) documentation page for information.

## Example: Adding a custom visualization file to your LookML project

Another option is to add the custom visualization JavaScript file to your LookML project using the Looker IDE:

  1. In the Looker IDE, [drag and drop](https://docs.cloud.google.com/looker/docs/ide-folders#uploading_files) the JavaScript file that defines your custom visualization into your LookML project.
  2. Optionally, [move the visualization file into a folder](https://docs.cloud.google.com/looker/docs/ide-folders#moving_items_in_a_foldered_project) in the Looker IDE, or [create a new folder](https://docs.cloud.google.com/looker/docs/ide-folders#creating_a_new_folder_in_the_ide) for the visualization file.
  3. Click on the visualization file in the file browser panel to display the file contents, then click **Save** to save the file.
  4. In the project's [manifest file](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files), define the visualization parameters. For example, this LookML adds a radial gauge custom visualization to the Looker project. The visualization is defined in a JavaScript file located in the `visualizations` directory of the LookML project:


    
    
      visualization: {
      id: "radial_gauge"
      label: "Radial Gauge"
      file: "visualizations/radialgauge_v2.js"
       }
    

  1. [Commit](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes) your changes and [deploy them to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production).

> You must deploy the visualization updates to see the customer visualization option in an Explore (saving the updates is not sufficient, even in Development Mode).




Once you have deployed your updates, Looker displays the name of the custom visualization as an option in the [**Visualization** tab](https://docs.cloud.google.com/looker/docs/creating-visualizations#choosing_a_visualization_type) of your project's Explores.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-cust-viz-718.png)

The visualization is also listed on the **Visualizations** page in the **Platform** section of Looker's **Admin** menu; see the [Admin settings - Visualizations](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations) documentation page for information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
