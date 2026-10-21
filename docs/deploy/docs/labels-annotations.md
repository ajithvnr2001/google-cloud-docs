---
url: https://docs.cloud.google.com/deploy/docs/labels-annotations/
title: Using annotations and labels with Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:49.547865+00:00
---

# Using annotations and labels with Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/labels-annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Using annotations and labels with Cloud Deploy Stay organized with collections  Save and categorize content based on your preferences. 

You can attach annotations and labels to your Cloud Deploy resources. They're not required.

This document lists the resources to which you can attach labels and annotations, and describes how you can use them and where you can view them.

## About annotations and labels

_Annotations_ are key-value pairs of free-form text. You can use them to attach arbitrary information associated with the resource.

You can use _labels_ to organize resources. For example, you can apply logic based on label selection.

As with annotations, labels are key-value pairs. But they must conform to the following limitations:

  * A Cloud Deploy resource can have no more than 64 labels.

  * Keys and values both must be 128 bytes or less.

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.

  * Keys must start with a lowercase letter or international character.

  * All characters must use UTF-8 encoding. International characters are allowed.




The `--labels` flag (for example, on `gcloud deploy releases create`) can take a list of key-value pairs:

`"name=wrench,mass=1.3kg,count=3"`

See the [Cloud Deploy API documentation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#resource:-deliverypipeline) for more details.

## Adding annotations and labels to Cloud Deploy resources

You can add annotations and labels to the following Cloud Deploy resources:

  * Delivery pipelines

For delivery pipelines, you add annotations and labels to the [YAML configuration file](https://docs.cloud.google.com/deploy/docs/config-files#structure_of_a_delivery_pipeline_configuration_file).



    
    
    apiVersion: deploy.cloud.google.com/v1
      kind: DeliveryPipeline
      metadata:
       name:
       annotations:
         key: "value"
       labels:
         key: "value"
      description:
      serialPipeline:
       stages:
       - targetId:
         profiles: []
       - targetId:
         profiles: []
    

  * Targets

Add annotations and labels to targets in the [target configuration YAML](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions).

For example, you can include a link to more information about third-party monitoring for your application. However, if the target is shared, remember that it could be used for more than one application, so the link should not be application specific.

  * Releases

You can add annotations or labels, or both, to a release using the `--labels` and `--annotations` flags on the `gcloud deploy releases create` command. Labels and annotations you add to a release are not carried forward as labels or annotations on resulting rollouts.

For example, you can use annotations to include a reference to a Git PR, author, or SHA hash of the Git commit containing the changes to be deployed. See [Using annotations to track the release's provenance](https://docs.cloud.google.com/deploy/docs/integrating-ci#using_annotations_to_track_the_releases_provenance) for more details.

  * Rollouts

You can add annotations and labels to new rollouts by specifying `--labels` or `--annotations` on the `gcloud deploy releases promote` command.

You can add annotations and labels to the first rollout by specifying `--initial-rollout-labels` or `--initial-rollout-annotations` on the `gcloud deploy releases create` command.

Some things you can do using annotations on a rollout:

    * Create an annotation containing the URL pointing to test results.
    * Create an annotation with a relevant ticket number from a workflow management system.

**Note:** labels and annotations added to Cloud Deploy resources are applied to those resources only. They're not transitively applied to deployed resources.

## Where can I find a resource's annotations?

You can view annotations and labels for any supported resource using the resource's `describe` command or by viewing the resource's metadata in Google Cloud console.

### From the gcloud CLI

To view a resource's annotations and labels from the command line, use a `describe` command on that resource. The following example shows the details for a target:
    
    
     $ gcloud deploy targets describe qsprod --delivery-pipeline=my-demo-app-1 \
                                                  --region=us-central1 \
                                                  --project=quickstart-basic8
    

The above command returns the following output:
    
    
     Target:
       annotations:
         approver_ticket_queue_url: https://workflows.example.com/deploy_approvals/4985729
       createTime: '2021-10-28T19:33:56.907887878Z'
       description: development cluster
       etag: 5b3bbee48f693cd7
       gke:
         cluster: projects/quickstart-basic8/locations/us-central1/clusters/quickstart-cluster-qsdev
       name: projects/quickstart-basic8/locations/us-central1/targets/qsdev
       uid: 3f3a5f8e7e0648e3bb17898ee531455d
       updateTime: '2021-11-10T16:55:11.502660604Z'
    

Notice that this output includes the `target_name` annotation.

### In Google Cloud console

To view annotations and labels for any Cloud Deploy resource that has such metadata, view that resource's details in Google Cloud console.

For example, here are the delivery pipeline details for a pipeline that includes an annotation:

![Delivery pipeline details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/delivery-pipeline-details1.png)

And here are the details for a release:

![Release details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/release-details2.png)

## Automatic labels from Cloud Deploy

By default, Cloud Deploy adds the following labels to rendered manifests:

  * `app.kubernetes.io/managed-by:`

A standard label to indicate deployment tooling. This is always set to `google-cloud-deploy` to identify the origin of the workload.

  * `deploy.cloud.google.com/location:`

The location of the deployed delivery pipeline, for example `us-central1`.

  * `deploy.cloud.google.com/project-id:`

The project ID of the deployed delivery pipeline.

  * `deploy.cloud.google.com/delivery-pipeline-id:`

The resource ID of the delivery pipeline used. This is taken from the [release snapshot](https://docs.cloud.google.com/deploy/docs/pipeline-instances).

  * `deploy.cloud.google.com/release-id:`

The resource ID of the deployed release.

  * `deploy.cloud.google.com/target-id:`

The resource ID of the deployment target. This is taken from the [release snapshot](https://docs.cloud.google.com/deploy/docs/pipeline-instances).




### Example usage

One example of using these automatically applied labels would be to create a graph within [Google Cloud Observability](https://cloud.google.com/products/operations) that aggregates [a container metric](https://cloud.google.com/monitoring/api/resources#tag_k8s_container) by Cloud Deploy properties:
    
    
    fetch k8s_container
    | metric 'kubernetes.io/container/cpu/core_usage_time'
    | filter metadata.user.c'app.kubernetes.io/managed-by' = "google-cloud-deploy"
    | group_by [
        pipeline: metadata.user.c'deploy.cloud.google.com/delivery-pipeline-id',
        target: metadata.user.c'deploy.cloud.google.com/target-id',
        release: metadata.user.c'deploy.cloud.google.com/release-id',],
          sum(val())
    | rate 1m
    

You can also use this with custom metrics. For example, if PodMonitor is configured with a label to match `app.kubernetes.io/managed-by: google-cloud-deploy`. You could then use a query to define a graph for custom metrics:
    
    
    fetch k8s_container
    | metric workload.googleapis.com/example_requests_total
    | filter metadata.user_labels.c'app.kubernetes.io/managed-by' = "google-cloud-deploy"
    | group_by [
        pipeline: metadata.user.c'deploy.cloud.google.com/delivery-pipeline-id',
        target: metadata.user.c'deploy.cloud.google.com/target-id',
        release: metadata.user.c'deploy.cloud.google.com/release-id',],
        sum(val())
    | rate 1m
    

### Disabling automatic labels

Your organization might disallow these automatic labels for regulatory, compliance, or other reasons. To support this, [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) offers a constraint that controls whether or not these labels are applied.

To prevent Cloud Deploy from automatically adding labels to rendered manifests, set Organization Policy Service constraint `clouddeploy.disableServiceLabelGeneration` to be enforced. Enforcing this constraint does not prevent you from manually specifying labels, nor does it remove labels from existing releases.

See [Using boolean constraints in organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) for more information on enabling constraints.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
