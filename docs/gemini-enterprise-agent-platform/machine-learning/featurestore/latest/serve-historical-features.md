---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/serve-historical-features/
title: Serve historical feature values \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:53.664182+00:00
---

# Serve historical feature values  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/serve-historical-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Serve historical feature values Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you need to retrieve or serve current as well as historical feature data, use offline serving to fetch feature values from BigQuery. For example, you can use offline serving to retrieve the feature values for specific timestamps to train a model.

All feature data, including historical feature data, is maintained in BigQuery, which constitutes the offline store for your feature values. To use offline serving, you must first register your BigQuery data source by creating feature groups and feature values. Also, in the case of offline serving, every row containing the same entity ID must have a different timestamp. For more information about data source preparation guidelines, see [Prepare data source](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/prepare-data-source).

## Before you begin

Authenticate to Gemini Enterprise Agent Platform, unless you've done so already.

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/authentication#local-development). 

## Fetch historical feature values

Use the following sample to fetch historical values from a feature from multiple entity IDs and timestamps.

### Python

Before trying this sample, follow the Python setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). For more information, see the [Agent Platform Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/authentication#client-libs). 
    
    
    import [bigframes](https://docs.cloud.google.com/python/docs/reference/bigframes/latest)
    import bigframes.pandas
    import pandas as pd
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    from vertexai.resources.preview.feature_store import (Feature, FeatureGroup, offline_store)
    from vertexai.resources.preview.feature_store import utils as fs_utils
    
    fg = FeatureGroup("FEATURE_GROUP_NAME")
    f1 = fg.get_feature("FEATURE_NAME_1")
    f2 = fg.get_feature("FEATURE_NAME_2")
    
    entity_df = pd.DataFrame(
      data={
        "ENTITY_ID_COLUMN": [
          "ENTITY_ID_1",
          "ENTITY_ID_2",
        ],
        "timestamp": [
          pd.Timestamp("FEATURE_TIMESTAMP_1"),
          pd.Timestamp("FEATURE_TIMESTAMP_2"),
        ],
      },
    )
    
    offline_store.fetch_historical_feature_values(
      entity_df=entity_df,
      features=[f1,f2],
    )
    

Replace the following:

  * FEATURE_GROUP_NAME: The name of the existing feature group containing the feature.

  * FEATURE_NAME_1 and FEATURE_NAME_2: The names of the registered features from which you want to retrieve the feature values.

  * ENTITY_ID_COLUMN: The name of the column containing the entity IDs. You can specify a column name only if it's registered in the feature group.

  * ENTITY_ID_1 and ENTITY_ID_2: The entity IDs for which you want to fetch the feature values. If you want to retrieve feature values for the same entity ID at different timestamps, specify the same entity ID corresponding to each timestamp.

  * FEATURE_TIMESTAMP_1 and FEATURE_TIMESTAMP_2: The timestamps corresponding to the historical feature values you want to retrieve. FEATURE_TIMESTAMP_1 corresponds to ENTITY_ID_1, FEATURE_TIMESTAMP_2 corresponds to ENTITY_ID_2, and so on. Specify the timestamps in the datetime format—for example, `2024-05-01T12:00:00`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
