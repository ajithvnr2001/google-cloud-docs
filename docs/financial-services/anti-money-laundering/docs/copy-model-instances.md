---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/copy-model-instances/
title: Copy models to new instances \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:23.799554+00:00
---

# Copy models to new instances  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/copy-model-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Copy models to new instances Stay organized with collections  Save and categorize content based on your preferences. 

The Copy Model API copies a model from one AML AI instance to another. This is typically done to copy a model from a consumer instance to a host instance after the model has been trained and evaluated. See also [Party registration sharing for multiple instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/registration-sharing).

The destination instance can be in a different Google Cloud project or a different Google Cloud region from the source instance, which lets you maintain a recoverable copy of a model outside its original region. For more information, see [Security and compliance features](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/security-and-compliance-features).

The copied model is stored separately from the source model. Deleting or updating the source model doesn't affect the copy, and you can delete the copy like any other AML AI resource.

## Copy an AML AI model to a different AML AI instance

When a model is copied from one instance to another, the copied model is identical to the source model with the following exceptions:

  * The source model field indicates the model was copied. The `satisfiesPzi` and `satisfiesPzs` fields in the model copy will be different from the source model to indicate the new model's GPS path. The `createTime` and `updateTime` fields in the model copy also vary from the source model.
  * The `engineVersion` field is updated to the local reference to the same engine version within the destination instance.



### Prerequisites

  * The user has the `financialservices.v1models.copyFrom` and `financialservices.v1models.copyTo` permissions on the source and destination instances respectively. This can be achieved for the instance by granting the role `roles/financialservices.admin` to the user on both source and destination project.
  * The source model exists.
  * The destination instance exists.
  * No model exists in the destination instance with the same name that will be used for the destination model.



### Copy request

Create a copy request to pass to the CopyModel request.

Before using any of the request data, make the following replacements:

  * DESTINATION_MODEL_ID: a user-defined identifier for the model in the destination instance.
  * SOURCE_PROJECT: the project that contains the instance where the model is copied from.
  * SOURCE_LOCATION: the location of the source model.
  * SOURCE_INSTANCE_ID: a user-defined identifier for the source instance that contains the source model.
  * SOURCE_MODEL_ID: a user-defined identifier for the source model.


    
    
     # Example request.json for copying a model:
      cat > request.json << 'EOF'
      {
       # The resource ID of the destination model which will exist under `parent` after the copy is complete.
       "model_id": "DESTINATION_MODEL_ID",
       "source_model": "projects/SOURCE_PROJECT/locations/SOURCE_LOCATION/instances/SOURCE_INSTANCE_ID/models/SOURCE_MODEL_ID"
      }
     EOF
    
    

Call the Financial Services API CopyModel request:
    
    
     curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d @request.json \
        "https://financialservices.googleapis.com/v1/projects/DESTINATION_PROJECT/locations/DESTINATION_LOCATION/instances/DESTINATION_INSTANCE_ID/models:copy"
    
    

## What's next

  * To generate predictions with the copied model, see [Create and manage prediction results](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-prediction-results).
  * To share registered parties between the source and destination instances, see [Party registration sharing for multiple instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/registration-sharing).
  * To learn how copying models fits into disaster recovery planning, see [Security and compliance features](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/security-and-compliance-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
