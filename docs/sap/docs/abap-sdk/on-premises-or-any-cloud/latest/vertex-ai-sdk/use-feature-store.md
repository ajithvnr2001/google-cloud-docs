---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/use-feature-store/
title: Use Agent Platform Feature Store \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:27.531570+00:00
---

# Use Agent Platform Feature Store  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/use-feature-store/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Use Agent Platform Feature Store Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-feature-store)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/use-feature-store)



This document describes how to use [Agent Platform Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview) to synchronize an online store, serve features from an online store, and search an online feature store using an entity or embeddings, by using the Agent Platform SDK for ABAP.

Feature Store is a managed, cloud-native service that lets you manage your machine learning (ML) feature data in a BigQuery table or view for online serving.

In a typical workflow of a Feature Store setup, you first prepare your SAP data source in BigQuery, register your data sources by creating feature groups and features, and set up online store and feature view resources. You can then serve the latest feature values online from a feature view or perform a similarity search on the online feature store. For information about how to set up your Feature Store, see [Agent Platform Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview).

Once your Feature Store is ready for online serving, you can use the Agent Platform SDK for ABAP for the following:

  * **Sync your online store:** Keep your online store consistent with your BigQuery data source for real-time serving during model prediction.
  * **Serve features:** Provide feature values from an online store for real-time applications.
  * **Search using an entity or embedding:** Retrieve a list of semantically similar or related entities from the online store.



## Before you begin

Before using the Agent Platform SDK for ABAP with Feature Store, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Installed](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#installation) the Agent Platform SDK for ABAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * Set up online feature serving. To learn how to create and use an online store to host and serve data in BigQuery with Feature Store in an end-to-end workflow, see [Jupyter Notebook tutorials for Feature Store](https://docs.cloud.google.com/vertex-ai/docs/tutorials/jupyter-notebooks).



## Instantiate the ABAP class for Feature Store

To use the Feature Store in your ABAP application, you instantiate the class `/GOOG/CL_FEATURE_STORE`.
    
    
    DATA(lo_client) = NEW /goog/cl_feature_store(
                              iv_key_name         = 'CLIENT_KEY'
                              iv_location         = 'LOCATION_ID'
                              iv_feature_store_id = 'FEATURE_ONLINE_STORE_NAME' ).
    

Replace the following:

  * `CLIENT_KEY`: The client key configured for authentication.
  * `LOCATION_ID`: Region where the online store is located, such as `us-central1`.
  * `FEATURE_ONLINE_STORE_NAME`: The name of the online store containing the feature view.



## Sync online store

To keep your online store consistent with your BigQuery data source for real-time serving during model prediction, sync the feature view resources in your online store with the feature data source in BigQuery.

### Before you begin

Because you access Feature Store through a regional endpoint, create an RFC destination to establish a connection to the Agent Platform API. You then specify the RFC destination in the service mapping table.

  1. Create an RFC destination for the Agent Platform API with the regional endpoint where your Feature Store resides. For example, if your Feature Store resides in `us-east1`, then the endpoint for the target host would be `us-east1-aiplatform.googleapis.com`. For information about regional endpoints, see [Service endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest#service-endpoint). To create an RFC destination, perform the following steps:

     1. In SAP GUI, execute the transaction code `SM59`.

     2. Create a new RFC destination. For the RFC destination that you created, make sure the **Connection Type** is set as follows: `G - HTTP connection to external server`.

     3. Go to the **Technical Settings** tab and enter the following details:

        * **Target Host** : Provide the regional endpoint where your Feature Store resides.

        * **Service No.** : Enter `443`. This port number is used for secure communication.

     4. Go to the **Logon & Security** tab and make sure that the **SSL Certificate** field is set with the option **DFAULT SSL Client (Standard)**.

     5. Save your changes.

  2. Configure the service mapping table for the Agent Platform API:

     1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

     2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Service Mapping**.

     3. Click **New Entries**.

     4. Specify the RFC destination for the Agent Platform API:

Name | Service Name | RFC Destination  
---|---|---  
Client key for authentication. | `aiplatform:v1` | Name of the RFC destination.  
     5. Save the new entry.




### Sync Feature Store

To start a data sync in a feature view, you use the `SYNC_FEATURE_DATA_TO_FS` method.
    
    
    DATA(lv_feature_view_sync_id) = lo_client->sync_feature_data_to_fs(
                                                 iv_feature_view_id = 'FEATURE_VIEW_NAME'
                                            )->get_feature_sync_id( ).
    

Replace `FEATURE_VIEW_NAME` with the name of the feature view for which you want to start the data sync.

This method returns a feature view sync ID, which you can use to check the status of the sync.

### Get the status of Feature Store sync

To get the status of a Feature Store sync, you can use the `GET_FEATURE_SYNC_STATUS` method.
    
    
    DATA(ls_status) = lo_client->get_feature_sync_status(
                                   iv_feature_view_id     = 'FEATURE_VIEW_NAME'
                                   iv_feature_sync_id     = 'FEATURE_VIEW_SYNC_ID'
                  )->get_feature_sync_status( ).
    

Replace the following:

  * `FEATURE_VIEW_NAME`: The name of the feature view for which you want to check the sync status.
  * `FEATURE_VIEW_SYNC_ID`: The feature view sync ID received from Feature Store.

This method returns one of the following statuses along with the error message, if any: `C: Complete`, `R: Running`, or `F: Failed`




### Sync Feature Store by using an SAP background job

To start a data sync in a feature view by using an SAP background job, use the `SYNC_FEATURE_DATA_TO_FS_BGJOB` method.

This method creates a background job in your SAP system, which starts the feature store sync and checks the status of the feature store sync every 30 seconds. If the feature store sync status is completed or failed, then the background job completes with a message accordingly. If the feature store sync is running, then the background job runs until the specified `TIMEOUT` value. After the timeout, the background job completes, but the feature store sync continues to run.
    
    
    DATA(ls_bgjob_details) = lo_client->sync_feature_data_to_fs_bgjob(
                                           iv_feature_view_id = 'FEATURE_VIEW_NAME'
                                           iv_timeout         = TIMEOUT
                                     )->get_background_job_details( ).
    

Replace the following:

  * `FEATURE_VIEW_NAME`: The name of the feature view for which you want to manually start the data sync.
  * `TIMEOUT`: Time in seconds after which the background job times out. This timeout doesn't impact the Feature Store sync.



This method returns a background job name and the corresponding ID. You can monitor this job from within SAP to check the status of the feature Store sync.

## Serve features from an online store

You can serve feature values from an online store for real-time applications, such as product recommendations. Depending on the type of online serving you've configured for your online store, you can serve feature values in one of the following ways:

  * Fetch feature values by using Bigtable online serving.
  * Fetch feature values by using Optimized online serving with a public endpoint.
  * Fetch feature values by using Optimized online serving with a Private Service Connect endpoint.



For more information about serving feature values, see [Serve features from an online store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/serve-feature-values).

### Before you begin

Before you can start serving feature values from an online store, retrieve the public endpoint domain name from the online store details, create an RFC destination for the endpoint, and then specify the RFC destination in the service mapping table.

  1. Retrieve the public endpoint domain name for the online store:

  2. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  3. Click **ABAP SDK for Google Cloud > Utilities > Agent Platform SDK: Get RFC information for Feature Store and Vector Search**.

  4. Select **Get Feature Store Details**.

  5. Enter the following parameters:

     * **Google Cloud Key Name** : The client key for authentication to Google Cloud.
     * **Location** : The region where the online store is located.
     * **Feature Store ID** : The name of the online store containing the feature view.
  6. Click **Execute** to view the details. Make a note of the public endpoint domain name next to the **Host** label.

  7. Create an RFC destination for the regional endpoint, public endpoint domain name, or the Private Service Connect endpoint of the online store. To create an RFC destination, perform the following steps:

  8. In SAP GUI, execute the transaction code `SM59`.

  9. Create a new RFC destination. For the RFC destination that you created, make sure the **Connection Type** is set as follows: `G - HTTP connection to external server`.

  10. Go to the **Technical Settings** tab and enter the following details:

     * **Target Host** : Provide the public endpoint domain name where your Feature Store resides.

     * **Service No.** : Enter `443`. This port number is used for secure communication.

  11. Go to the **Logon & Security** tab and make sure that the **SSL Certificate** field is set with the option **DFAULT SSL Client (Standard)**.

  12. Save your changes.

  13. Configure the service mapping table for the Agent Platform API:

  14. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  15. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Service Mapping**.

  16. Click **New Entries**.

  17. Specify the RFC destination for the Agent Platform API:

Name | Service Name | RFC Destination  
---|---|---  
Client key for authentication. | `apiinvoker:v1` | Name of the RFC destination.  
  18. Save the new entry.




### Fetch feature values

In Feature Store, an _entity_ refers to an item that you want to track features for, such as a customer, a product, or any other data point. Each entity is associated with a set of features and their corresponding values.

To fetch feature values by specifying a single entity ID, use the method `SERVE_FEATURE_VALUES`.
    
    
    DATA(lt_features) = lo_client->serve_feature_values(
                             iv_feature_view_id = 'FEATURE_VIEW_NAME'
                                 it_entity_id       = 'ENTITY_ID'
                    )->get_features( ).
    

Replace the following:

  * `FEATURE_VIEW_NAME`: The name of the feature view from which you want to serve feature values.
  * `ENTITY_ID`: The value of the ID column in the feature record from which you want to serve the latest feature values. Alternatively, you can provide an array of parts to construct the Entity ID. Ensure that the ID columns are in the same order as defined in the feature view.



## Search for approximate nearest neighbors

For online stores created for optimized online serving, you can perform a vector similarity search to retrieve a list of semantically similar or related entities, also called approximate nearest neighbors. You can search for approximate nearest neighbors based on either an entity ID or an embedding.

### Before you begin

When you create an online store for optimized online serving, Feature Store generates a public endpoint domain name for the online store. Before you can start searching for the nearest neighbors from a feature view in the online store, you need to retrieve the public endpoint domain name from the online store details, create an RFC destination for the endpoint, and then specify the RFC destination in the service mapping table.

  1. Retrieve the public endpoint domain name for the online store:

     1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

     2. Click **ABAP SDK for Google Cloud > Utilities > Agent Platform SDK: Get RFC information for Feature Store and Vector Search**.
     3. Select **Get Feature Store Details**.
     4. Enter the following parameters:

        * **Google Cloud Key Name** : The client key for authentication to Google Cloud.
        * **Location** : The region where the online store is located.
        * **Feature Store ID** : The name of the online store containing the feature view.
     5. Click **Execute** to view the details. Make a note of the public endpoint domain name next to the **Host** label.

  2. Create an RFC destination for the public endpoint domain name of the online store:

     1. In SAP GUI, execute the transaction code `SM59`.

     2. Create a new RFC destination. For the RFC destination that you created, make sure the **Connection Type** is set as follows: `G - HTTP connection to external server`.

     3. Go to the **Technical Settings** tab and enter the following details:

        * **Target Host** : Provide the public endpoint domain name for the online store.

        * **Service No.** : Enter `443`. This port number is used for secure communication.

     4. Go to the **Logon & Security** tab and make sure that the **SSL Certificate** field is set with the option **DFAULT SSL Client (Standard)**.

     5. Save your changes.

  3. Configure the service mapping table for the Agent Platform API:

     1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

     2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Service Mapping**.
     3. Click **New Entries**.
     4. Specify the RFC destination for the Agent Platform API:

Name | Service Name | RFC Destination  
---|---|---  
Client key for authentication. | `apiinvoker:v1` | Name of the RFC destination.  
     5. Save the new entry.




### Retrieve nearest neighbor matches of an embedding

You can search for semantically related entities by specifying an embedding.

To search nearest neighbors for an embedding, send a request by using the `SEARCH_USING_EMBEDDINGS` method.
    
    
    DATA(lt_embeddings) = VALUE /goog/cl_aiplatform_v1=>ty_t_/goog/num_float( EMBEDDING_DATA ).
    
    DATA(lt_neighbours) = lo_client->search_using_embeddings(
      EXPORTING
        iv_feature_view_id = 'FEATURE_VIEW_NAME'
        it_embeddings      = lt_embeddings
        is_search_params   = VALUE #( neighbor_count     = 'NEIGHBOR_COUNT'
                                      return_full_entity = 'RETURN_FULL_ENTITY' )
    )->get_neighbours( ).
    

Replace the following:

  * `EMBEDDING_DATA`: The embedding for which you want to retrieve the approximate nearest neighbor matches. An embedding is represented by an array of float values.
  * `FEATURE_VIEW_NAME`: The name of the feature view where you want to search for approximate nearest neighbor matches.
  * `NEIGHBOR_COUNT`: Number of approximate nearest neighbors you want to retrieve.
  * `RETURN_FULL_ENTITY`: Optional. Specify whether you want to include or exclude the features for the entities in the response. To include the features along with the entities in the response, enter `ABAP_TRUE`. The default value is `ABAP_FALSE`.



### Retrieve nearest neighbor matches of an entity

You can search for semantically related entities by specifying an entity ID.

To search nearest neighbors for an entity ID, send a request by using the `SEARCH_USING_ENTITY` method.
    
    
    DATA(lt_neighbours) = lo_client->search_using_entity(
      EXPORTING
        iv_feature_view_id = 'FEATURE_VIEW_NAME'
        iv_entity_id       = 'ENTITY_ID'
        is_search_params   = VALUE #( neighbor_count     = 'NEIGHBOR_COUNT'
                                      return_full_entity = 'RETURN_FULL_ENTITY' )
    )->get_neighbours( ).
    

Replace the following:

  * `FEATURE_VIEW_NAME`: The name of the feature view where you want to search for approximate nearest neighbor matches.
  * `ENTITY_ID:`: Entity ID of the entity for which you want to retrieve approximate nearest neighbor matches.
  * `NEIGHBOR_COUNT`: Number of approximate nearest neighbors that you want to retrieve.
  * `RETURN_FULL_ENTITY`: Optional. Specify whether you want to include or exclude the features for the entities in the response. To include the features along with the entities in the response, enter `ABAP_TRUE`. The default value is `ABAP_FALSE`.



## What's next

  * Learn about [application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
