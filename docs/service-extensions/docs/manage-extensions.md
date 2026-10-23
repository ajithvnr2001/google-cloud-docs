---
url: https://docs.cloud.google.com/service-extensions/docs/manage-extensions/
title: Manage extensions \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:22.531804+00:00
---

# Manage extensions  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/manage-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Manage extensions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage extensions that are [configured using Service Extensions](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service).

For a product overview, see [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).

**Note:** Authorization extensions are not supported using the Google Cloud console.

## List extensions

### Console

  1. Go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

A list of the extensions in your project appears in a sortable table that shows the following information:

     * **Name** : the name of the extension
     * **Product** : the Google Cloud product that uses the extension
     * **Type** : the type of extension
     * **Region** : the region for regional load balancers
     * **Extensions** : the number of extension chains
     * **In use by** : the forwarding rules with which the extension is associated
     * **Last modified** : the time when the extension was last modified
  2. Optional: To filter the list, do the following:

     1. To see a list of properties, click next to **Filter table**.

     2. From the list, select a property.

The property name, followed by a colon, appears next to the **Filter table** label.

     3. To see a list of values that match the property, insert a space next to the colon, and then select a value from the list.

     4. Optional: To specify combined filters, enter the `OR` operator between property-value pairs.

  3. Optional: To perform other operations with a selected extension, click more_vert**More actions** , and then select an option:

     * To [edit the extension](https://docs.cloud.google.com/service-extensions/docs/manage-extensions#modify-extension), click **Edit**.
     * To [delete the extension](https://docs.cloud.google.com/service-extensions/docs/manage-extensions#delete-extension), click **Delete**.



### gcloud

### Authorization extensions

To list the authorization extensions in the current project, use the [`gcloud service-extensions authz-extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/authz-extensions/list).
    
    
    gcloud service-extensions authz-extensions list \
        --location LOCATION
    

Replace `LOCATION` with the location of the extension resource.

The following high-level information is provided about each extension: the name, the authorization policy, and the last modified date.

### Edge extensions

To list the edge extensions in the current project, use the [`gcloud service-extensions lb-edge-extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-edge-extensions/list).
    
    
    gcloud service-extensions lb-edge-extensions list \
        --location LOCATION
    

Replace `LOCATION` with the location of the extension resource.

The following high-level information is provided about each extension: the name, the load-balancing scheme, and the last modified date.

### Route extensions

To list the route extensions in the current project, use the [`gcloud service-extensions lb-route-extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/list).
    
    
    gcloud service-extensions lb-route-extensions list \
        --location LOCATION
    

Replace `LOCATION` with the location of the extension resource.

The following high-level information is provided about each extension: the name, the load-balancing scheme, and the last modified date.

### Traffic extensions

To list the traffic extensions in the current project, use the [`gcloud service-extensions lb-traffic-extensions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-traffic-extensions/list).
    
    
    gcloud service-extensions lb-traffic-extensions list \
      --location LOCATION
    

Replace `LOCATION` with the location of the extension resource.

The following high-level information is provided about each extension: the name, the load-balancing scheme, and the last modified date.

## View the details of an extension

### Console

  1. Go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the name of the extension for which you want to see details.

The **Details** page for the extension opens. It has the following sections:

     * **Basics** : This section shows these basic details about the extension: the product, the load balancer, the extension type, the description, and labels.

     * **Forwarding rules** : This section provides a link to the associated forwarding rules. You can click the link to view its details.

     * **Extension** or **Extension chains** : This section shows the details of an extension (if only one extension was specified) or extension chains in the specified sequence (if multiple extensions were specified). Additionally, for each extension or extension chain, the match condition is indicated. For each extension, the details mentioned include the extension name, the programmability type, metadata, headers, events, and other information.




### gcloud

### Authorization extensions

To view the details of an authorization extension, use the [`gcloud service-extensions authz-extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/authz-extensions/describe).
    
    
    gcloud service-extensions authz-extensions describe EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the route extension
  * `LOCATION`: the location of the extension resource



### Edge extensions

To view the details of an edge extension, use the [`gcloud service-extensions lb-edge-extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-edge-extensions/describe).
    
    
    gcloud service-extensions lb-edge-extensions describe EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the edge extension
  * `LOCATION`: the location of the extension resource



### Route extensions

To view the details of a route extension, use the [`gcloud service-extensions lb-route-extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/describe).
    
    
    gcloud service-extensions lb-route-extensions describe EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the route extension
  * `LOCATION`: the location of the extension resource



### Traffic extensions

To view the details of a traffic extension, use the [`gcloud service-extensions lb-traffic-extensions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-traffic-extensions/describe).
    
    
    gcloud service-extensions lb-traffic-extensions describe EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the traffic extension
  * `LOCATION`: the location of the backend



## Edit an extension

### Console

  1. Go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. For the extension that you want to edit, click more_vert**More actions** , and then select **Edit**.

Alternatively, click the extension name, and then, on the **Details** page, click **Edit**.

On the **Edit service extensions** page, the basic information about the extension isn't editable. You can edit other details.

  3. Make changes as required.

For information about most fields, see the pages on how to configure [route extensions](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions) and [traffic extensions](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions).

  4. Click **Update extension**.




### gcloud

To edit an extension, use the same steps that you used to configure it. For more information, see the pages about how to configure [route extensions](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions), [authorization extensions](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions), and [traffic extensions](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions).

**Note:** You can't modify the extension name or the load balancing scheme of an existing extension.

## Delete an extension

### Console

  1. Go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. For the extension that you want to delete, select the checkbox, and then click **Delete** at the top of the page.

Alternatively, click more_vert**More actions** , and then select **Delete**.

  3. In the confirmation message box, to confirm the operation, click **Delete**.




### gcloud

### Authorization extensions

To delete a authorization extension, use the [`gcloud service-extensions authz-extensions delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/authz-extensions/delete).
    
    
    gcloud service-extensions authz-extensions delete EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the authorization extension
  * `LOCATION`: the location of the backend



### Edge extensions

To delete an edge extension, use the [`gcloud service-extensions lb-edge-extensions delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-edge-extensions/delete).
    
    
    gcloud service-extensions lb-edge-extensions delete EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the edge extension
  * `LOCATION`: the location of the backend



### Route extensions

To delete a route extension, use the [`gcloud service-extensions lb-route-extensions delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/delete).
    
    
    gcloud service-extensions lb-route-extensions delete EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the route extension
  * `LOCATION`: the location of the backend



### Traffic extensions

To delete a traffic extension, use the [`gcloud service-extensions lb-traffic-extensions delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-traffic-extensions/delete).
    
    
    gcloud service-extensions lb-traffic-extensions delete EXTENSION_ID \
        --location LOCATION
    

Replace the following:

  * `EXTENSION_ID`: the ID or the fully qualified name of the traffic extension
  * `LOCATION`: the location of the backend



## What's next

  * [Manage plugins](https://docs.cloud.google.com/service-extensions/docs/manage-plugins)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
