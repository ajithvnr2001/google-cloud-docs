---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-delete-model/
title: Delete an online prediction model \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:44.654877+00:00
---

# Delete an online prediction model  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-delete-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Delete an online prediction model Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Online Prediction is a Preview feature that is available as-is and is not recommended for production environments. Google provides no service-level agreements (SLA) or technical support commitments for Preview features. For more information, see GDC's [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

This page describes the process to delete an online prediction model and all the resources associated with it.

## Before you begin

To get the permissions that you need to access Online Prediction, ask your IAM Project Admin to grant you the Vertex AI Prediction User (`vertex-ai-prediction-user`) role.

For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

Additionally, to get the permissions that you need to delete objects in a bucket, ask your IAM Project Admin to grant you the Project Bucket Object Admin (`project-bucket-object-admin`) role in the project.

## Delete resources

If you want to delete an online prediction model and all the resources associated with it, perform the following steps:

  1. Delete the `DeployedModel` custom resource associated with your model on the prediction cluster:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG delete -f DEPLOYED_MODEL_NAME.yaml
         

Replace the following:

     * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
     * `DEPLOYED_MODEL_NAME`: the name of the `DeployedModel` definition file.
  2. Edit the `Endpoint` custom resource in one of the following ways:

     * If the endpoint that the `DeployedModel` uses doesn't host other models, delete the `Endpoint` custom resource on the prediction cluster:
           
           kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG delete -f ENDPOINT_NAME.yaml
           

Replace `ENDPOINT_NAME` with the name of the `Endpoint` definition file.

     * If the endpoint that the `DeployedModel` uses hosts other models, perform the following steps:

       1. Update the `Endpoint` custom resource on the prediction cluster:
              
              kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG edit -f ENDPOINT_NAME.yaml
              

Replace `ENDPOINT_NAME` with the name of the `Endpoint` definition file.

       2. On the YAML file, manually delete the `serviceRef` object containing the `DeployedModel` reference you deleted previously.

       3. Save the changes on the YAML file.

  3. Delete your model from the storage bucket. For more information about how to delete objects from storage buckets, see [Delete storage objects in projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/delete-storage-objects).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
