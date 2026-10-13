---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-connection/
title: connection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.593790+00:00
---

# connection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  connection Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    
    connection: "connection_name"
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `connection` |  Default Value None Accepts A string containing the name of a connection   
---|---  
  
## Definition

`connection` specifies the database connection from which a model will retrieve data. Database connections are defined and named on the [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) page in the **Database** section of Looker's **Admin** panel.

**Important:** Each model can specify only one connection. If you want to use multiple database connections in a project, you must create a different model file for each connection.

When a Looker developer defines a connection in a model file using the `connection` parameter, the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide) displays a drop-down that suggests database connections that are available on the instance.

## Example

In the `ecommerce.model.lookml` file, specify that the model should retrieve data from the `ecommerce_events` connection:
    
    
    connection: "ecommerce_events"
    

## Common challenges

### `connection` must reference a connection name from Looker's admin settings

The connection name that is referenced by `connection` does not take the name of an actual database or schema. The name must be one of the connections that is available when you're [configuring a model](https://docs.cloud.google.com/looker/docs/manage-projects#adding_and_editing_configurations) or on the [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) page in Looker's **Admin** panel.

### If a model configuration exists, then `connection` can only reference an allowed connection

If a Looker developer specifies a connection in the model file that is not allowed in the model configuration, then any query on that model will not run.

### If a model configuration does not exist, then only certain people can query

If you have not been given the [`manage_models` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) (which is included in the admin role) then the model must be configured before you can run queries on the model.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
