---
url: https://docs.cloud.google.com/deployment-manager/docs/deployments/add-labels-deployments/
title: Adding Labels to a Deployment \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:35.297302+00:00
---

# Adding Labels to a Deployment  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/deployments/add-labels-deployments/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Adding Labels to a Deployment Stay organized with collections  Save and categorize content based on your preferences. 

Labels are a lightweight way to organize deployments that are related or associated with each other. For example, a common practice is to label deployments that are intended for production, staging, or development separately, so you can easily search for deployments that belong to each stage when necessary.

## What are labels?

A label is a key-value pair that you can assign to Google Cloud deployments. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

## Requirements for labels

The labels applied to a resource must meet the following requirements:

  * Each resource can have up to 64 labels.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty, and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. Keys must start with a lowercase letter or international character.
  * The key portion of a label must be unique within a single resource. However, you can use the same key with multiple resources.



These limits apply to the key and value for each label, and to the individual Google Cloud resources that have labels. There is no limit on how many labels you can apply across all resources within a project.

## Common uses of labels

Here are some common use cases for labels:

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish deployments owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Creating a deployment with labels

When creating a deployment, you can add labels by providing one or more key value pairs as labels when you create your deployment. If you have an existing deployment, you can update the deployment to add new labels or change existing labels.

You must use the gcloud CLI or the API to create a deployment with labels.

###  gcloud 

In `gcloud`, add labels to your deployment by providing the `--labels` flag, followed by a comma-separated list of key value pairs. For example, the following command adds two labels to the deployment, `environment=production` and `storage=media`:
    
    
    gcloud deployment-manager deployments create example-deployment --config example-config.yaml \
        --labels environment=production,storage=media
    

To see the labels applied to the deployment, get a description of the deployment:
    
    
    gcloud deployment-manager deployments describe example-deployment
    ---
    fingerprint: 0p03t0z31PQLOrGH8KdhWQ==
    id: '2204841443843636456'
    insertTime: '2017-04-18T09:42:47.323-07:00'
    labels:
    - key: environment
      value: production
    - key: storage
      value: media
    manifest: manifest-1492533767362
    name: example-deployment
    operation:
      endTime: '2017-04-18T09:43:04.581-07:00'
      name: operation-1492533767010-54d7398ff76d1-7930b926-f64e72ae
      operationType: insert
      progress: 100
      startTime: '2017-04-18T09:42:48.034-07:00'
      status: DONE
      user:user@example.com
    

###  API 

In the API, follow the instructions to [create your deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments#creating_a_deployment) and include the new `labels` property in your request body. For example:
    
    
    {
      "name": "example-deployment",
      "target": {
        "config": {
          "content": "..."
          },
       }
      "labels": [
      {
        "key": "environment",
        "value": "production"
      },
      {
        "key": "storage",
        "value": "media"
      }
     ]
    }
    

## Removing labels

###  Console 

  1. Go to the **Deployments** page in the Google Cloud console.

[Go to the Deployments page](https://console.cloud.google.com/deployments)

  2. If prompted, select your project and click **Continue**.

  3. Check the box next to the deployment that you want to remove labels from. A side panel appears.

  4. Click **X** next to each label you want to remove.

  5. Save your changes.




###  gcloud 

In `gcloud`, remove labels by using the `deployments update` command and supplying the `--remove-labels` flag, followed by a comma-separated list of label keys to remove.

For example, the following removes a label with the `environment` key:
    
    
    gcloud deployment-manager deployments update example-deployment --remove-labels environment
    

###  API 

In the API, follow the instructions to [update your deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments#creating_a_deployment) and include an update to your deployment that does not contain the `labels` property in your request body, effectively removing labels.

## Adding or updating labels

You can add new labels or update labels on existing deployments.

###  Console 

  1. Go to the **Deployments** page in the Google Cloud console.

[Go to the Deployments page](https://console.cloud.google.com/deployments)

  2. If prompted, select your project and click **Continue**.

  3. Check the box next to the deployment you want to update labels from. A side panel opens.

  4. To change label values, update the appropriate label entries. If you want to change the label key, you will need to delete the label and add it again with the new key.

  5. Save your changes.




###  gcloud 

In `gcloud`, update or add new labels by using the `deployments update` command and supplying the `--update-labels` flag, followed by a comma-separated list of the updated labels:

For example, the following updates the `environment` label:
    
    
    gcloud deployment-manager deployments update example-deployment --update-labels environment=production
    

###  API 

In the API, follow the instructions to [update your deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments#creating_a_deployment) and in your request body, omit the `labels` property, which removes labels from the deployment.

## Adding labels during deployment previews

Before you create a deployment, you can [preview](https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file) the deployment. As part of the preview, you can assign labels to the previewed deployment. For example:
    
    
    gcloud deployment-manager deployments create example-deployment --config example-config.yaml \
        --labels environment=production --preview
    

To change labels during preview, you must [update](https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file#previewmultiple) the preview with the new labels. To learn more about previews, read the [Previewing a Configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file) documentation.

## Filtering searches using labels

You can search your resources and filter results by labels.

###  Console 

  1. Go to the **Deployments** page in the Google Cloud console.

[Go to the Deployments page](https://console.cloud.google.com/deployments)

  2. If prompted, select your project and click **Continue**.

  3. In the search bar, start typing `labels.` and the search bar will automatically list labels that you can filter on.




###  gcloud 

In `gcloud`, make a `list` request and use the `--filter` flag. To filter on labels, use the syntax `labels.[KEY]=[VALUE]`. For example, if you wanted to filter on a label with `environment` as the key and `production` as the value, you can run this command:
    
    
    gcloud deployment-manager deployments list --filter labels.environment=production
    

For complete documentation about the filter syntax in the gcloud CLI, see the [`gcloud topic filters` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

###  API 

In the API, make a list request with a URL encoded `filter` query parameter. For example, to filter based on a label key `environment` being equal to value `production`, make the following `GET` request:
    
    
    GET https://www.googleapis.com/deploymentmanager/v2/deployments/list?filter=labels.environment+eq+production
    

For more information, read the [`filter` documentation](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/list#filter) in the API reference.

## What's next

  * Learn how to [delete your deployments](https://docs.cloud.google.com/deployment-manager/docs/deployments/deleting-deployments).
  * Learn more about [updating existing deployments](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
