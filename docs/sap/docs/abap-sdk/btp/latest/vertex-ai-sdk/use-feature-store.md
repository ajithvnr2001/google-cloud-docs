---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-feature-store/
title: Use Agent Platform Feature Store \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:37.028630+00:00
---

# Use Agent Platform Feature Store  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-feature-store/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Use Agent Platform Feature Store Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/use-feature-store)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/use-feature-store)



This document describes how to use [Agent Platform Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview) to synchronize an online store, serve features from an online store, and search an online feature store using an entity or embeddings, by using the Agent Platform SDK for ABAP.

Feature Store is a managed, cloud-native service that lets you manage your machine learning (ML) feature data in a BigQuery table or view for online serving.

In a typical workflow of a Feature Store setup, you first prepare your SAP data source in BigQuery, register your data sources by creating feature groups and features, and set up online store and feature view resources. You can then serve the latest feature values online from a feature view or perform a similarity search on the online feature store. For information about how to set up your Feature Store, see [Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview).

Once your Feature Store is ready for online serving, you can use the Agent Platform SDK for ABAP for the following:

  * **Sync your online store:** Keep your online store consistent with your BigQuery data source for real-time serving during model prediction.
  * **Serve features:** Provide feature values from an online store for real-time applications.
  * **Search using an entity or embedding:** Retrieve a list of semantically similar or related entities from the online store.



## Before you begin

Before using the Agent Platform SDK for ABAP with Feature Store, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Installed](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#installation) the Agent Platform SDK for ABAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
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

Because you access Feature Store through a regional endpoint, create a communication system and a communication arrangement, and configure the client key accordingly.

  1. Access the SAP Fiori launchpad of the BTP ABAP system where the ABAP SDK for Google Cloud is installed.

  2. Go to **All spaces > Administration > Communication Management**.

  3. Create a communication system:

     1. Open the **Communication Systems** app.
     2. Click **New**.
     3. In the **New Communication System** dialog that appears, enter a value for the following fields:

        * **System ID** : enter a system ID.
        * **System name** : enter a system name.
     4. Click **Create**.

     5. In the **Host name** field, enter the URL for the regional endpoint. For example, if your Feature Store resides in `us-east1`, then the endpoint for the target host is `us-east1-aiplatform.googleapis.com`. For information about regional endpoints, see [Service endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest#service-endpoint).

     6. In the **Port** field, enter `443`.

     7. On the **Users for Outbound Communication** tab, click **Add**.

     8. For the **Authentication method** field, select **None**.

     9. Click **Save**.

  4. Create a communication arrangement:

     1. Open the **Communication Arrangement** app.
     2. Click **New**.
     3. In the **New Communication Arrangement** dialog that appears, enter a value for the following fields:

        * **Scenario** : select **Authentication using Workload Identity Federation** (`/GOOG/COM_SDK_SRV`).
        * **Arrangement name** : enter a name for the communication arrangement.
     4. Click **Create**.

     5. For the communication arrangement entry that appears, in the **Communication System** field, select the communication system that you created in the previous step.

     6. Click **Save**.

  5. Create a client key and a communication map:

     1. Go to the space that contains the SAP Fiori apps for SDK configuration.
     2. Open the **Google SDK: Main Configuration** app.
     3. Click **Create**.
     4. In the **Create** dialog that appears, enter a client key name.
     5. Click **Continue**.
     6. Enter a value for the following fields:

        * **Service account** : enter the service account that is granted access to the Google Cloud APIs.
        * **Project ID** : enter the project ID of the Google Cloud project where you've enabled the Google Cloud APIs. For information about project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Project number** : enter the project number of the Google Cloud project where you've enabled the Google Cloud APIs. For information about project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Authentication type** : select **W (Workload Identity Federation)**.
     7. For the communication map for the default entry of service name as "authentication", provide the communication arrangement you have set up for the WIF-based authentication.

     8. Add one more entry to the communication map and choose service as `aiplatform:v1` and provide the communication arrangement as the one you just created.

     9. Click **Create**. A dialog appears confirming that you agree to use the ABAP SDK for Google Cloud under standard Google Cloud terms.

     10. To validate the authentication configuration, click **Check connection**. A green check for an entry indicates a successful configuration.

In case of any errors, see the [troubleshooting](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting) guide for information about resolving common errors.




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
  * `FEATURE_VIEW_SYNC_ID`: The feature view sync ID received from Sync Feature Store.

This method returns one of the following statuses along with the error message, if any: `C: Complete`, `R: Running`, or `F: Failed`




## Serve features from an online store

You can serve feature values from an online store for real-time applications, such as product recommendations. Depending on the type of online serving you've configured for your online store, you can serve feature values in one of the following ways:

  * Fetch feature values by using Bigtable online serving.
  * Fetch feature values by using Optimized online serving with a public endpoint.
  * Fetch feature values by using Optimized online serving with a Private Service Connect endpoint.



For more information about serving feature values, see [Serve features from an online store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/serve-feature-values).

### Before you begin

Before you can start serving feature values from an online store, retrieve the public endpoint domain name from the online store details. Then, create a communication system and a communication arrangement, and configure them in the client key configuration by using the **Google SDK: Main Configuration** SAP Fiori app.

  1. To retrieve the public endpoint, create the `ZCL_GET_FEATURE_STORE_PUB_EP` in a local package of your choosing. Pass a valid client key, the store ID, and the location of the Feature Store.
         
         CLASS zcl_get_feature_store_pub_ep DEFINITION
         PUBLIC FINAL
         CREATE PUBLIC.
         PUBLIC SECTION.
            INTERFACES if_oo_adt_classrun.
         ENDCLASS.
         CLASS zcl_get_feature_store_pub_ep IMPLEMENTATION.
         METHOD if_oo_adt_classrun~main.
            DATA lv_ckey        TYPE /goog/keyname.
            DATA lv_location_id TYPE string.
            DATA lv_fsid        TYPE string.
            DATA lv_project_id  TYPE string.
            DATA lv_msg         TYPE string.
         
            "TODO:Developer - Pass relevant values
            lv_ckey = 'CLIENT_KEY'.
            lv_fsid = 'FEATURE_ONLINE_STORE_NAME'.
            lv_location_id = 'LOCATION_ID'.
            TRY.
               DATA(lo_aip) = NEW  /goog/cl_aiplatform_v1( iv_key_name = lv_ckey ).
               lv_project_id = lo_aip->gv_project_id.
               " Call API method: aiplatform.projects.locations.featureOnlineStores.get
               lo_aip->get_feature_online_stores( EXPORTING iv_p_projects_id              = lv_project_id
                                                            iv_p_locations_id             = lv_location_id
                                                            iv_p_feature_online_stores_id = lv_fsid
                                                   IMPORTING es_output                     = DATA(ls_output)
                                                            ev_ret_code                   = DATA(lv_ret_code)
                                                            ev_err_text                   = DATA(lv_err_text) ).
               IF lo_aip->is_success( lv_ret_code ) = abap_true.
                  out->write( | Public endpoint is| ).
                  out->write( ls_output-dedicated_serving_endpoint-public_endpoint_domain_name ).
               ENDIF.
               CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
               lv_msg = lo_cx_sdk->get_text( ).
               out->write( |Exception occurred, reason: { lv_msg }| ).
            ENDTRY.
         ENDMETHOD.
         ENDCLASS.
         

  2. Activate and execute the `ZCL_GET_FEATURE_STORE_PUB_EP` class.

The output, which is the public endpoint of your online store, uses the following format:
         
         xxxxxxxxxx.LOCATION_ID-PROJECT_ID.featurestore.vertexai.goog
         

This output includes the following values:

     * `LOCATION_ID`: the region where your online store is located.
     * `PROJECT_ID`: the project ID of the Google Cloud project where your online store is located.
  3. Access the SAP Fiori launchpad of the BTP ABAP system where the ABAP SDK for Google Cloud is installed.

  4. Go to **All spaces > Administration > Communication Management**.

  5. Create a communication system:

     1. Open the **Communication Systems** app.
     2. Click **New**.
     3. In the **New Communication System** dialog that appears, enter a value for the following fields:

        * **System ID** : enter a system ID.
        * **System name** : enter a system name.
     4. Click **Create**.

     5. In the **Host name** field, enter the public endpoint that you retrieved by executing the `ZCL_GET_FEATURE_STORE_PUB_EP` class in a preceding step.

     6. In the **Port** field, enter `443`.

     7. Go to the **Users for Outbound Communication** tab, and click **Add**.

     8. In the **Authentication method** field, select **None**.

     9. Click **Save**.

  6. Create a communication arrangement:

     1. Open the **Communication Arrangements** app.
     2. Click **New**.
     3. In the **New Communication Arrangement** dialog that appears, enter a value for the following fields:

        * **Scenario** : select **Authentication using Workload Identity Federation (`/GOOG/COM_SDK_SRV`)**.
        * **Arrangement name** : enter a name for the communication arrangement.
     4. Click **Create**.

     5. For the communication arrangement entry that appears, in the **Communication System** field, select the communication system that you created in the previous step.

     6. Click **Save**.

  7. Create a client key and communication map:

     1. Go to the space that contains the SAP Fiori apps for SDK configuration.
     2. Open the **Google SDK: Main Configuration** app.
     3. Click **Create**.
     4. In the **Create** dialog that appears, enter a client key name.
     5. Click **Continue**.
     6. Enter the following details:

        * **Service account** : enter the service account that is granted access to the Google Cloud APIs.
        * **Project ID** : enter the project ID of the Google Cloud project where you've enabled the Google Cloud APIs. For information about project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Project number** : enter the project number of the Google Cloud project where you've enabled the Google Cloud APIs. For information about project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Authentication type** : select **W (Workload Identity Federation)**.
     7. For the communication map for the default entry of service name as "authentication", provide the communication arrangement you have set up for the WIF-based authentication.

     8. Add one more entry to the communication map and choose service as `aiplatform:v1` and provide the communication arrangement as the one you just created.

     9. Click **Create**. A dialog appears confirming that you agree to use the ABAP SDK for Google Cloud under standard Google Cloud terms.

     10. To validate the authentication configuration, click **Check connection**. A green check for an entry indicates a successful configuration.

In case of any errors, see the [troubleshooting](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting) guide for information about resolving common errors.

  8. Verify that your communication map contains the following three entries:

Service name | Communication scenario | Communication arrangement  
---|---|---  
`authentication` | `/GOOG/SDK_COM_WIF` | Communication arrangement that you've created for the `XSUAA` service.   
`aiplatform:v1` | `/GOOG/COM_SDK_SRV` | Communication arrangement that you've set by using the communication system that contains the regional endpoint for `AI PLATFORM`.  
`apiinvoker:v1` | `/GOOG/COM_SDK_SRV` | Communication arrangement that you've set up by using the communication system for the public endpoint for the Feature Store serving in the previous step.  



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

Before you can start searching for approximate nearest neighbors from a feature view in the online store, retrieve the public endpoint domain name from the online store details. Then, create a communication system and a communication arrangement, and configure them in the client key configuration by using the **Google SDK: Main Configuration** SAP Fiori app.

  1. To retrieve the public endpoint, create the `ZCL_GET_FEATURE_STORE_PUB_EP` in a local package of your choosing. Pass a valid client key, the store ID, and the location of the Feature Store.
         
         CLASS zcl_get_feature_store_pub_ep DEFINITION
         PUBLIC FINAL
         CREATE PUBLIC.
         PUBLIC SECTION.
            INTERFACES if_oo_adt_classrun.
         ENDCLASS.
         CLASS zcl_get_feature_store_pub_ep IMPLEMENTATION.
         METHOD if_oo_adt_classrun~main.
            DATA lv_ckey        TYPE /goog/keyname.
            DATA lv_location_id TYPE string.
            DATA lv_fsid        TYPE string.
            DATA lv_project_id  TYPE string.
            DATA lv_msg         TYPE string.
         
            "TODO:Developer - Pass relevant values
            lv_ckey = 'CLIENT_KEY'.
            lv_fsid = 'FEATURE_ONLINE_STORE_NAME'.
            lv_location_id = 'LOCATION_ID'.
            TRY.
               DATA(lo_aip) = NEW  /goog/cl_aiplatform_v1( iv_key_name = lv_ckey ).
               lv_project_id = lo_aip->gv_project_id.
               " Call API method: aiplatform.projects.locations.featureOnlineStores.get
               lo_aip->get_feature_online_stores( EXPORTING iv_p_projects_id              = lv_project_id
                                                            iv_p_locations_id             = lv_location_id
                                                            iv_p_feature_online_stores_id = lv_fsid
                                                   IMPORTING es_output                     = DATA(ls_output)
                                                            ev_ret_code                   = DATA(lv_ret_code)
                                                            ev_err_text                   = DATA(lv_err_text) ).
               IF lo_aip->is_success( lv_ret_code ) = abap_true.
                  out->write( | Public endpoint is| ).
                  out->write( ls_output-dedicated_serving_endpoint-public_endpoint_domain_name ).
               ENDIF.
               CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
               lv_msg = lo_cx_sdk->get_text( ).
               out->write( |Exception occurred, reason: { lv_msg }| ).
            ENDTRY.
         ENDMETHOD.
         ENDCLASS.
         

  2. Activate and execute the `ZCL_GET_FEATURE_STORE_PUB_EP` class.

The output, which is the public endpoint of your online store, uses the following format:
         
         xxxxxxxxxx.LOCATION_ID-PROJECT_ID.featurestore.vertexai.goog
         

This output includes the following values:

     * `LOCATION_ID`: the region where your online store is located.
     * `PROJECT_ID`: the project ID of the Google Cloud project where your online store is located.
  3. Access the SAP Fiori launchpad of the BTP ABAP system where the ABAP SDK for Google Cloud is installed.

  4. Go to **All spaces > Administration > Communication Management**.

  5. Create a communication system:

     1. Open the **Communication Systems** app.
     2. Click **New**.
     3. In the **New Communication System** dialog that appears, enter a value for the following fields:

        * **System ID** : enter a system ID.
        * **System name** : enter a system name.
     4. Click **Create**.

     5. In the **Host name** field, enter the public endpoint that you retrieved by executing the `ZCL_GET_FEATURE_STORE_PUB_EP` class in a preceding step.

     6. In the **Port** field, enter `443`.

     7. Go to the **Users for Outbound Communication** tab, and click **Add**.

     8. In the **Authentication method** field, select **None**.

     9. Click **Save**.

  6. Create a communication arrangement:

     1. Open the **Communication Arrangements** app.
     2. Click **New**.
     3. In the **New Communication Arrangement** dialog that appears, enter a value for the following fields:

        * **Scenario** : select **Authentication using Workload Identity Federation (`/GOOG/COM_SDK_SRV`)**.
        * **Arrangement name** : enter a name for the communication arrangement.
     4. Click **Create**.

     5. For the communication arrangement entry that appears, in the **Communication System** field, select the communication system that you created in the previous step.

     6. Click **Save**.

  7. Create a client key and communication map:

     1. Go to the space that contains the SAP Fiori apps for SDK configuration.
     2. Open the **Google SDK: Main Configuration** app.
     3. Click **Create**.
     4. In the **Create** dialog that appears, enter a client key name.
     5. Click **Continue**.
     6. Enter the following details:

        * **Service account** : enter the service account that is granted access to the Google Cloud APIs.
        * **Project ID** : enter the project ID of the Google Cloud project where you've enabled the Google Cloud APIs. For information about project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Project number** : enter the project number of the Google Cloud project where you've enabled the Google Cloud APIs. For information about project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Authentication type** : select **W (Workload Identity Federation)**.
     7. For the communication map for the default entry of service name as "authentication", provide the communication arrangement you have set up for the WIF-based authentication.

     8. Add one more entry to the communication map and choose service as `aiplatform:v1` and provide the communication arrangement as the one you just created.

     9. Click **Create**. A dialog appears confirming that you agree to use the ABAP SDK for Google Cloud under standard Google Cloud terms.

     10. To validate the authentication configuration, click **Check connection**. A green check for an entry indicates a successful configuration.

In case of any errors, see the [troubleshooting](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting) guide for information about resolving common errors.

  8. Verify that your communication map contains the following three entries:

Service name | Communication scenario | Communication arrangement  
---|---|---  
`authentication` | `/GOOG/SDK_COM_WIF` | Communication arrangement that you've created for the `XSUAA` service.   
`aiplatform:v1` | `/GOOG/COM_SDK_SRV` | Communication arrangement that you've set by using the communication system that contains the regional endpoint for `AI PLATFORM`.  
`apiinvoker:v1` | `/GOOG/COM_SDK_SRV` | Communication arrangement that you've set up by using the communication system for the public endpoint for the Feature Store serving in the previous step.  



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

  * Learn about [application development with the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
