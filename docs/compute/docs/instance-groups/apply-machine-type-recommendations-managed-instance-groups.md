---
url: https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups/
title: Apply machine type recommendations to MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:15.632046+00:00
---

# Apply machine type recommendations to MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Apply machine type recommendations to MIGs Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine provides machine type recommendations for managed instance groups (MIGs) to help you improve workload performance and cost efficiency. Use these recommendations to determine whether you should resize the machine type of your instances to add or remove vCPU and memory resources.

To learn more about the available machine types for VM instances, read the [machine types](https://docs.cloud.google.com/compute/docs/machine-resource) documentation.

Machine type recommendations are also known as _rightsizing recommendations_.

**Note:** These recommendations do not change the number of instances in a managed instance group.

## Before you begin

  * Read the [Google Cloud console](https://docs.cloud.google.com/compute/docs/console) documentation.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Restrictions

Recommendations are available for managed instance groups that are in a single zone and aren't autoscaled or load balanced.

## Pricing

Machine type recommendations are available free of charge. If you apply a recommendation to resize your instance's machine type, you are charged for the machine type that you choose.

## Use cases

You can take advantage of machine type recommendations if you have the following workload conditions:

  * Workloads with periodic increases and decreases in traffic, such as workloads susceptible to seasonal traffic.
  * Workloads that are underutilized in CPU and RAM because they are bounded by other limitations, such as read/write throughput.
  * Workloads that run software that requires individual software licenses and that can't add more instances; in this case, you might rely on machine type recommendations to scale your machine types while keeping the number of VM instances constant.
  * Workloads that are unable to dynamically adapt to a changing number of instances, such as workloads that aren't a good fit for autoscaling.



You might not want to use machine type recommendations for any of the following reasons:

  * Your workloads have very brief CPU spikes. Because machine type recommendations are based on average CPU utilization over 60-second intervals, recommendations might not be generated quickly enough to capture shorter spikes. Apps with short usage spikes might need to run on a larger machine type than the recommended one, or you can [enable autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) to accommodate these spikes.
  * Your load spikes occur less frequently than once in 8 days (for example, monthly). Infrequent spikes are overlooked by the rightsizing algorithm, which only looks at the last 8 days of history.
  * Each instance in your MIG handles a drastically different workload. In such a situation, the recommendations optimize for the VM instances with the highest load, which would oversize most VM instances in the group.
  * Your MIG has underutilized VMs because it does not serve live load and is intended to provide ready-to-serve failover capacity.
  * Your MIG has oversized VMs for one of the following reasons: 
    * Your software licensing requires a minimum machine size.
    * You need to meet storage or networking IOPS requirements that are only available with a minimum machine type.



## How machine type recommendations work

Compute Engine monitors the CPU and memory utilization of running virtual machines and makes recommendations using the last 8 days of data. To recommend the best single machine type for all instances in a managed instance group, Compute Engine generates a standard machine type recommendation for individual instances and, after adjusting for outliers, chooses a machine type that does not undersize any single VM instance. Any instances that aren't running, such as stopped or restarting VM instances, aren't included in the calculation.

Compute Engine might make recommendations similar to the following:

  * If your instance group has had low CPU utilization most of the time, Compute Engine recommends a machine type with fewer virtual CPUs.
  * If your instance group has had high CPU utilization most of the time, Compute Engine recommends a machine type with more virtual CPUs.
  * If your instance group hasn't used a large fraction of its memory, Compute Engine recommends a machine type with less memory.
  * If your instance group has actively been using a large fraction of its memory most of the time. Compute Engine recommends a machine type with more memory.

**Note:** Compute Engine uses the same CPU utilization numbers reported on the Compute Engine dashboard to determine the recommendations to make. These numbers are based on the average utilization of your instances over 60-second intervals, so they do not capture short CPU usage spikes. Apps with short CPU spikes might need to run on a larger machine type than the one recommended by Google, or you can enable autoscaling to accommodate these spikes.

Compute Engine might make recommendations to use either a standard or custom machine type. Note that there are some limitations in the amount of memory and vCPU available to a machine. In particular, increasing one resource might require increasing the other at the same time to follow the [specifications](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications) of a valid machine type. Also, Compute Engine only recommends machine types that are available in the zone where the instance is running.

For more information, see [Custom machine type specifications](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications).

If the workload for the managed instance group is very different across individual instances, some instances might be oversized so that the fully utilized instances have enough resources according to the recommendation. For example, Compute Engine might make the following recommendation to support the workload of instance 4 even though instances 1, 2, 3, and 5 might be oversized and underutilized:

Recommendations made for a managed instance group[ ![Example of oversizing due to different workloads across managed instances](https://docs.cloud.google.com/static/compute/images/mig-recs.svg)](https://docs.cloud.google.com/static/compute/images/mig-recs.svg)

For this reason, recommendations for a managed instance group work best when the instances have a reasonably distributed workload.

For cost difference estimations, the cost of an instance group is based on the previous week's usage (before sustained use discount) and is extrapolated to 30 days. This is then compared to the recommended machine type monthly cost (before sustained use discount). For accurate pricing and details, read the [pricing documentation](https://cloud.google.com/compute/vm-instance-pricing).

## View machine type recommendations

Compute Engine makes recommendations available through the [Google Cloud console](https://console.cloud.google.com/). You can view machine type recommendations through the [Recommender](https://docs.cloud.google.com/recommender/docs) using the gcloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeInstanceGroupManagerMachineTypeRecommendations.list` on the project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Select your project and click **Continue**.
  3. Look at the **Recommendation** column to review recommendations for individual managed instance groups. You can also sort the column by amount of estimated savings. If there are no recommendations next to the instance groups, Compute Engine does not have any recommendations to make.

![Recommendations column.](https://docs.cloud.google.com/static/compute/images/recommendations-column.png)

  4. If your instance group has two instance templates, Compute Engine provides recommendations for each instance template. Click a recommendation to view recommendations for the respective instance template.

![Recommendations for multiple templates](https://docs.cloud.google.com/static/compute/images/multiple-templates.png)




###  gcloud 

Use the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command and specify the [VM managed instance group rightsizing recommender](https://docs.cloud.google.com/recommender/docs/vm-instance-group-rightsizing-recommender).
    
    
    gcloud recommender recommendations list \
          --recommender=google.compute.instanceGroupManager.MachineTypeRecommender \
          --project [PROJECT_ID] \
          --location [ZONE] \
          --format=yaml
    

For example:
    
    
    gcloud recommender recommendations list \
        --recommender=google.compute.instanceGroupManager.MachineTypeRecommender \
        --project my-project \
        --location us-central1-a \
        --format=yaml
    

The response includes the following fields for each recommendation:

  * [`operationGroups`](https://docs.cloud.google.com/recommender/docs/key-concepts#operation_groups): groups of operations that you can perform in serial order to apply the recommendation.
  * `description`: a human-readable explanation of the recommendation.


    
    
    ---
    content:
      ...
      operationGroups:
      - operations:
        - action: test
          path: /properties/machineType
          resource: //compute.googleapis.com/projects/my-project/global/instanceTemplates/my-old-template
          resourceType: compute.googleapis.com/InstanceTemplate
          value: n1-standard-4
        - action: copy
          path: /
          resource: //compute.googleapis.com/projects/my-project/global/instanceTemplates/$new-it-name
          resourceType: compute.googleapis.com/InstanceTemplate
          sourcePath: /
          sourceResource: //compute.googleapis.com/projects/my-project/global/instanceTemplates/my-old-template
        - action: replace
          path: /name
          resource: //compute.googleapis.com/projects/my-project/global/instanceTemplates/$new-it-name
          resourceType: compute.googleapis.com/InstanceTemplate
          value: $new-it-name
        - action: replace
          path: /properties/machineType
          resource: //compute.googleapis.com/projects/my-project/global/instanceTemplates/$new-it-name
          resourceType: compute.googleapis.com/InstanceTemplate
          value: custom-2-5632
      - operations:
        - action: replace
          path: /versions/*/name
          pathValueMatchers:
            versions/*/instanceTemplate:
              matchesPattern: .*global/instanceTemplates/my-old-template
          resource: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instanceGroupManagers/example-group
          resourceType: compute.googleapis.com/InstanceGroupManager
          value: global/instanceTemplates/$new-it-name
    ...
    description: Save cost by changing machine type from n1-standard-4 to custom-2-5120.
    ...
    name: projects/823742397239/locations/us-central1-a/recommenders/google.compute.instanceGroupManager.MachineTypeRecommender/recommendations/c50a1c41-7e65-417d-a32e-45248a2cb318
    ...
    

For more information, see the [Recommender](https://docs.cloud.google.com/recommender/docs/using-api) docs.

###  REST 

Use the [Recommender API](https://docs.cloud.google.com/recommender/docs/vm-instance-group-rightsizing-recommender) with the MIG machine type recommender ID.
    
    
    PROJECT_ID=my-project
    LOCATION=us-central1-c
    RECOMMENDER_ID=google.compute.instanceGroupManager.MachineTypeRecommender
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      https://recommender.googleapis.com/v1/projects/$PROJECT_ID/locations/$LOCATION/recommenders/$RECOMMENDER_ID/recommendations
    

The response includes the following fields for each recommendation:

  * `name` The name of the recommendation
  * `description` A human-readable explanation of the recommendation.
  * [`operationGroups`](https://docs.cloud.google.com/recommender/docs/key-concepts#operation_groups) Groups of operations that you can perform in serial order to apply the recommendation.



For more information, see the [Recommender](https://docs.cloud.google.com/recommender/docs/using-api) docs.

When you create a new managed instance group, recommendations for the new group appear 24 hours after the group has been created.

Afterward, recommendations are refreshed at regular intervals throughout the day.

## Apply recommendations to instance groups

**Note:** You might have valid reasons for running a particular instance group at very low or very high utilization. Machine type recommendations are suggestions to help you more efficiently use your instances, but they might not be appropriate for every situation. For example, if you expect your VM instances to be heavily utilized at startup, you should never apply recommendations because, after a period of time, the recommendations don't take into account the high utilization required for startup. Applying recommendations could cause you to resize your instances below the capacity the instances need to boot up, preventing the instances from booting up successfully the next time they're restarted.

If you want to apply the recommendations made by Compute Engine, you can resize the managed instances directly from the console. Alternatively, you can manually step through the resizing operations yourself. The Recommender API returns a series of resizing operations; see [Operation groups](https://docs.cloud.google.com/recommender/docs/key-concepts#operation_groups) for more information.

When you apply a recommendation to a managed instance group, you perform the following operations:

  1. Clones the instance templates being used by the managed instance group.
  2. Modifies the cloned instance templates based on the recommendations and any changes you want to make.
  3. Uses the [managed instance group updater](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) to apply the new template. If the instance group has two instance templates:

     1. You can only apply recommendations for one instance template at a time.
     2. A managed instance group can maintain at most two instance templates at a time, so you cannot apply a recommendation while still maintaining two other instance templates. However, you can apply a recommendation if your instance group only has one instance template.

**Caution:** Applying a recommendation causes Compute Engine to actively delete and create new instances to replace your existing instances. This is a potentially disruptive action for your instance group, so make sure you prepare appropriately. Compute Engine attempts to alleviate some of these concerns by allowing you to [control the rate of the update](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#options).

To resize managed instances directly from the console:

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the recommendation text for the instance group that you want to update.

![Selecting a recommendation column.](https://docs.cloud.google.com/static/compute/images/select-recommendation.png)

  3. A pop-up appears with more detail and a choice to **Cancel** , **Dismiss** the recommendation, or **Continue**. To review and apply the recommendation, click **Continue**.

  4. In the **Review recommendation** page, the recommendation is explained in detail. If you continue with the recommendation, Compute Engine updates all instances in the instance group with the old template to the new template.

  5. (Advanced) To customize how the new template is rolled out to your instances, click **Customize deployment**. The **Deployment configuration** screen appears.

**Note:** All of the following options are available through the [Managed Instance Group Updater](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups).
     1. If you want to actively delete and create instances using the new instance template, choose **Automatic**. If you want to only apply the update when the instance is created by other means, such as a resize or when a new instance is added to the group, choose **Selective**.
     2. If you select automatic updates, choose if you want to **Keep instance names when replacing instances**. 
        * If you choose to keep instance names, under **Temporary additional instances** , choose how many temporary extra instances to create above the managed instance group's target size. The more instances you allow, the faster your update is, at the cost of additional instances. The default is 1 additional instance.
     3. Under **Maximum unavailable instances** , choose how many instances can be offline at a time during this update. This number also includes any instances that are unavailable for other reasons. For example, if the instance group is in the process of being resized up, instances in the middle of being created might be unavailable; these instances would count toward this number. The default is 1 instance that can be unavailable at a time.
     4. Optional: Expand **Show advanced options**. Under **Minimum wait time** , choose how many seconds to wait before marking a new instance as updated. The time starts after a successful health check. Use this feature to control the rate at which the instance template is applied.
  6. To apply the changes, click **Save**.

  7. When you are ready to deploy the changes, click **Deploy**.




## Dismiss recommendations

When you have finished using a recommendation, you can dismiss it from the console. Within the console, dismissing removes a recommendation from the total savings estimate and also minimizes the appearance of the recommendation by turning it grey.

Dismissing a recommendation through the console doesn't affect the list of recommendations that is returned by the [Recommender API](https://docs.cloud.google.com/recommender/docs). To manage the state of recommendations returned by the Recommender API, see [Using the API](https://docs.cloud.google.com/recommender/docs/using-api).

To dismiss a single recommendation from the console:

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the recommendation text you want to dismiss. A pop-up appears with more details and a **Dismiss** button.

  3. Click **Dismiss**.


**Note:** Dismissing a recommendation de-emphasizes it in the table but does not hide it.

To restore a recommendation in the console:

  1. On the **Instance groups** page, click the grey recommendation text you want to restore.

![Dismissed recommendation.](https://docs.cloud.google.com/static/compute/images/mig-recs-gray.png)

  2. A pop-up appears with more detail and a **Restore** button.

  3. Click **Restore**.




## Use the monitoring agent for more precise recommendations

Cloud Monitoring offers a [monitoring agent](https://docs.cloud.google.com/monitoring/agent) that collects additional disk, CPU, network, and process metrics from your VM instances. You can install the monitoring agent on your VM instances so it can access system resources and application services to collect this data.

If the Monitoring agent is installed and running on a VM instance, the CPU and memory metrics collected by the agent are automatically used to compute machine type recommendations. The [agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent) provided by the Monitoring agent give better insights into resource utilization of the instance than the default Compute Engine metrics. This lets the recommendation engine estimate resource requirements better and make more precise recommendations.

To install the agent, see [Installing the Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent/install-agent).

**Note:** Metric data from the Cloud Monitoring agent is priced by volume on a sliding scale. For details, see the [pricing](https://cloud.google.com/stackdriver/pricing#monitoring-costs) documentation.

## What's next

  * Learn more about [changing the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) of an instance.
  * Read about what happens when you [stop an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).
  * See how you can [apply recommendations to individual VM instances](https://docs.cloud.google.com/compute/docs/instances/apply-sizing-recommendations-for-instances).
  * Learn more about the [Recommender](https://docs.cloud.google.com/recommender/docs) and its [API](https://docs.cloud.google.com/recommender/docs/using-api).
  * Learn about [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) as an alternative to machine type resizing.
  * Learn more about [recommendation insights](https://docs.cloud.google.com/compute/docs/instance-groups/view-and-understand-mig-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
