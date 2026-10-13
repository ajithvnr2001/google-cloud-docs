---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/
title: Vertex AI Search for commerce API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:11.623250+00:00
---

# Vertex AI Search for commerce API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Vertex AI Search for commerce API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/retail.svg)](https://www.npmjs.org/package/@google-cloud/retail)

Vertex AI Search for commerce API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/CHANGELOG.md).

  * [Vertex AI Search for commerce API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/retail/latest)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Versioning

  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Vertex AI Search for commerce API API](https://console.cloud.google.com/flows/enableapi?apiid=retail.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/retail
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
export analytics metrics | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/analytics_service.export_analytics_metrics.js)  
add catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.add_catalog_attribute.js)  
get attributes config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.get_attributes_config.js)  
get completion config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.get_completion_config.js)  
get default branch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.get_default_branch.js)  
list catalogs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.list_catalogs.js)  
remove catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.remove_catalog_attribute.js)  
replace catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.replace_catalog_attribute.js)  
set default branch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.set_default_branch.js)  
update attributes config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.update_attributes_config.js)  
update catalog | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.update_catalog.js)  
update completion config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/catalog_service.update_completion_config.js)  
complete query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/completion_service.complete_query.js)  
import completion data | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/completion_service.import_completion_data.js)  
create control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/control_service.create_control.js)  
delete control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/control_service.delete_control.js)  
get control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/control_service.get_control.js)  
list controls | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/control_service.list_controls.js)  
update control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/control_service.update_control.js)  
conversational search | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/conversational_search_service.conversational_search.js)  
batch update generative question configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/generative_question_service.batch_update_generative_question_configs.js)  
get generative questions feature config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/generative_question_service.get_generative_questions_feature_config.js)  
list generative question configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/generative_question_service.list_generative_question_configs.js)  
update generative question config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/generative_question_service.update_generative_question_config.js)  
update generative questions feature config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/generative_question_service.update_generative_questions_feature_config.js)  
create model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.create_model.js)  
delete model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.delete_model.js)  
get model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.get_model.js)  
list models | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.list_models.js)  
pause model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.pause_model.js)  
resume model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.resume_model.js)  
tune model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.tune_model.js)  
update model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/model_service.update_model.js)  
predict | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/prediction_service.predict.js)  
add fulfillment places | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.add_fulfillment_places.js)  
add local inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.add_local_inventories.js)  
create product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.create_product.js)  
delete product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.delete_product.js)  
get product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.get_product.js)  
import products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.import_products.js)  
list products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.list_products.js)  
purge products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.purge_products.js)  
remove fulfillment places | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.remove_fulfillment_places.js)  
remove local inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.remove_local_inventories.js)  
set inventory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.set_inventory.js)  
update product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/product_service.update_product.js)  
search | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/search_service.search.js)  
add control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/serving_config_service.add_control.js)  
create serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/serving_config_service.create_serving_config.js)  
delete serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/serving_config_service.delete_serving_config.js)  
get serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/serving_config_service.get_serving_config.js)  
list serving configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/serving_config_service.list_serving_configs.js)  
remove control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/serving_config_service.remove_control.js)  
update serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/serving_config_service.update_serving_config.js)  
collect user event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/user_event_service.collect_user_event.js)  
import user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/user_event_service.import_user_events.js)  
purge user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/user_event_service.purge_user_events.js)  
rejoin user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/user_event_service.rejoin_user_events.js)  
write user event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2/user_event_service.write_user_event.js)  
export analytics metrics | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/analytics_service.export_analytics_metrics.js)  
get branch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/branch_service.get_branch.js)  
list branches | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/branch_service.list_branches.js)  
add catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.add_catalog_attribute.js)  
batch remove catalog attributes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.batch_remove_catalog_attributes.js)  
get attributes config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.get_attributes_config.js)  
get completion config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.get_completion_config.js)  
get default branch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.get_default_branch.js)  
list catalogs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.list_catalogs.js)  
remove catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.remove_catalog_attribute.js)  
replace catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.replace_catalog_attribute.js)  
set default branch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.set_default_branch.js)  
update attributes config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.update_attributes_config.js)  
update catalog | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.update_catalog.js)  
update completion config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/catalog_service.update_completion_config.js)  
complete query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/completion_service.complete_query.js)  
import completion data | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/completion_service.import_completion_data.js)  
create control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/control_service.create_control.js)  
delete control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/control_service.delete_control.js)  
get control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/control_service.get_control.js)  
list controls | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/control_service.list_controls.js)  
update control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/control_service.update_control.js)  
conversational search | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/conversational_search_service.conversational_search.js)  
batch update generative question configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/generative_question_service.batch_update_generative_question_configs.js)  
get generative questions feature config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/generative_question_service.get_generative_questions_feature_config.js)  
list generative question configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/generative_question_service.list_generative_question_configs.js)  
update generative question config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/generative_question_service.update_generative_question_config.js)  
update generative questions feature config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/generative_question_service.update_generative_questions_feature_config.js)  
create merchant center account link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/merchant_center_account_link_service.create_merchant_center_account_link.js)  
delete merchant center account link | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/merchant_center_account_link_service.delete_merchant_center_account_link.js)  
list merchant center account links | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/merchant_center_account_link_service.list_merchant_center_account_links.js)  
create model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.create_model.js)  
delete model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.delete_model.js)  
get model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.get_model.js)  
list models | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.list_models.js)  
pause model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.pause_model.js)  
resume model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.resume_model.js)  
tune model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.tune_model.js)  
update model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/model_service.update_model.js)  
predict | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/prediction_service.predict.js)  
add fulfillment places | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.add_fulfillment_places.js)  
add local inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.add_local_inventories.js)  
create product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.create_product.js)  
delete product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.delete_product.js)  
export products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.export_products.js)  
get product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.get_product.js)  
import products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.import_products.js)  
list products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.list_products.js)  
purge products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.purge_products.js)  
remove fulfillment places | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.remove_fulfillment_places.js)  
remove local inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.remove_local_inventories.js)  
set inventory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.set_inventory.js)  
update product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/product_service.update_product.js)  
accept terms | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.accept_terms.js)  
enroll solution | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.enroll_solution.js)  
get alert config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.get_alert_config.js)  
get logging config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.get_logging_config.js)  
get project | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.get_project.js)  
list enrolled solutions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.list_enrolled_solutions.js)  
update alert config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.update_alert_config.js)  
update logging config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/project_service.update_logging_config.js)  
search | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/search_service.search.js)  
add control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/serving_config_service.add_control.js)  
create serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/serving_config_service.create_serving_config.js)  
delete serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/serving_config_service.delete_serving_config.js)  
get serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/serving_config_service.get_serving_config.js)  
list serving configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/serving_config_service.list_serving_configs.js)  
remove control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/serving_config_service.remove_control.js)  
update serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/serving_config_service.update_serving_config.js)  
collect user event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/user_event_service.collect_user_event.js)  
export user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/user_event_service.export_user_events.js)  
import user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/user_event_service.import_user_events.js)  
purge user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/user_event_service.purge_user_events.js)  
rejoin user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/user_event_service.rejoin_user_events.js)  
write user event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2alpha/user_event_service.write_user_event.js)  
export analytics metrics | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/analytics_service.export_analytics_metrics.js)  
add catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.add_catalog_attribute.js)  
batch remove catalog attributes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.batch_remove_catalog_attributes.js)  
get attributes config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.get_attributes_config.js)  
get completion config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.get_completion_config.js)  
get default branch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.get_default_branch.js)  
list catalogs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.list_catalogs.js)  
remove catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.remove_catalog_attribute.js)  
replace catalog attribute | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.replace_catalog_attribute.js)  
set default branch | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.set_default_branch.js)  
update attributes config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.update_attributes_config.js)  
update catalog | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.update_catalog.js)  
update completion config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/catalog_service.update_completion_config.js)  
complete query | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/completion_service.complete_query.js)  
import completion data | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/completion_service.import_completion_data.js)  
create control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/control_service.create_control.js)  
delete control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/control_service.delete_control.js)  
get control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/control_service.get_control.js)  
list controls | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/control_service.list_controls.js)  
update control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/control_service.update_control.js)  
conversational search | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/conversational_search_service.conversational_search.js)  
batch update generative question configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/generative_question_service.batch_update_generative_question_configs.js)  
get generative questions feature config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/generative_question_service.get_generative_questions_feature_config.js)  
list generative question configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/generative_question_service.list_generative_question_configs.js)  
update generative question config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/generative_question_service.update_generative_question_config.js)  
update generative questions feature config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/generative_question_service.update_generative_questions_feature_config.js)  
create model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.create_model.js)  
delete model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.delete_model.js)  
get model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.get_model.js)  
list models | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.list_models.js)  
pause model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.pause_model.js)  
resume model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.resume_model.js)  
tune model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.tune_model.js)  
update model | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/model_service.update_model.js)  
predict | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/prediction_service.predict.js)  
add fulfillment places | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.add_fulfillment_places.js)  
add local inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.add_local_inventories.js)  
create product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.create_product.js)  
delete product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.delete_product.js)  
export products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.export_products.js)  
get product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.get_product.js)  
import products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.import_products.js)  
list products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.list_products.js)  
purge products | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.purge_products.js)  
remove fulfillment places | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.remove_fulfillment_places.js)  
remove local inventories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.remove_local_inventories.js)  
set inventory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.set_inventory.js)  
update product | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/product_service.update_product.js)  
get alert config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/project_service.get_alert_config.js)  
update alert config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/project_service.update_alert_config.js)  
search | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/search_service.search.js)  
add control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/serving_config_service.add_control.js)  
create serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/serving_config_service.create_serving_config.js)  
delete serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/serving_config_service.delete_serving_config.js)  
get serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/serving_config_service.get_serving_config.js)  
list serving configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/serving_config_service.list_serving_configs.js)  
remove control | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/serving_config_service.remove_control.js)  
update serving config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/serving_config_service.update_serving_config.js)  
collect user event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/user_event_service.collect_user_event.js)  
export user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/user_event_service.export_user_events.js)  
import user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/user_event_service.import_user_events.js)  
purge user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/user_event_service.purge_user_events.js)  
rejoin user events | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/user_event_service.rejoin_user_events.js)  
write user event | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-retail/samples/generated/v2beta/user_event_service.write_user_event.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/retail@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md` and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template.

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
