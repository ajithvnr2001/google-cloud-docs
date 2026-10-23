---
url: https://docs.cloud.google.com/run/docs/configuring/scaling-controls/
title: Configure custom scaling controls for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:53.572978+00:00
---

# Configure custom scaling controls for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/scaling-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure custom scaling controls for services Stay organized with collections  Save and categorize content based on your preferences. 

By default, Cloud Run optimizes for high performance with a utilization target of 60% for both CPU and concurrency, and scales the number of instances automatically to handle all incoming requests. However, for some use cases, you might want the ability to configure which scaling factors to use, such as CPU only, and set custom targets for utilization.

Cloud Run provides scaling controls to give you more ownership of your service's scaling behaviors, letting you make informed decisions about scaling your workload according to your requirements. You can configure the following custom utilization targets:

  * Target utilization for CPU-based scaling
  * Target utilization for concurrency-based scaling



With scaling controls, you can optimize costs and improve predictability for your services. For more information about the default autoscaling behavior of Cloud Run services, see [About instance autoscaling in Cloud Run services](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).

## Configuration limits

The following limits apply to custom scaling targets:

Scaling driver | Default % | Minimum configurable % | Maximum configurable %  
---|---|---|---  
`CPU target utilization` | 60% | 10% | 90%  
`Concurrency target utilization` | 60% | 10% | 95%  
  
## Configure custom targets

Define custom utilization targets to optimize costs or improve performance for your workloads by configuring specific CPU and concurrency utilization targets within the configuration limits.

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

Even if you configure custom concurrency targets or disable CPU-based scaling, Adaptive Concurrency Tuning (ACT) remains active. For details, see [About instance autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling#adaptive-concurrency).

You can configure scaling controls using the Google Cloud console, gcloud CLI, YAML, or Terraform when you [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision).

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. If you are configuring a new service, click **Deploy container** to display the **Create service** page.

  3. If you are configuring an existing service, click the service to open its **Service details** page, then click the **Scaling** tab.

  4. Locate the **Service scaling** section. Make sure **Auto scaling** is selected. Expand the **Customize autoscaling factors** section to configure the following utilization targets:

     * To configure target CPU utilization, click **CPU utilization** and enter a value from `10` to `90`.

     * To configure target concurrency utilization, click **Concurrent request utilization** and enter a value from `10` to `95`.

     * Click **Done** under each utilization configuration.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

Update the [target CPU utilization](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--scaling-cpu-target) and the [target concurrency utilization](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--scaling-concurrency-target) values of a given revision by running the `gcloud run services update` command.

  * To update the target CPU utilization, run the following command:
        
        gcloud run services update SERVICE --scaling-cpu-target=CPU_TARGET

Replace the following:

    * SERVICE: the name of your service.

    * CPU_TARGET: the target for CPU utilization. Specify a value from `0.1` to `0.90`. You can only configure up to two digits after the decimal point.

  * To update the target concurrency utilization, run the following command:
        
        gcloud run services update SERVICE --scaling-concurrency-target=CONCURRENCY_TARGET

Replace the following:

    * SERVICE: the name of your service.

    * CONCURRENCY_TARGET: the target for concurrency utilization. Specify a value from `0.1` to `0.95`. You can only configure up to two digits after the decimal point.

  * To update both the target CPU and the concurrency utilization, run the following command:
        
        gcloud run services update SERVICE --scaling-cpu-target=CPU_TARGET \
        --scaling-concurrency-target=CONCURRENCY_TARGET

Replace the following:

    * SERVICE: the name of your service.
    * CPU_TARGET: the target for CPU utilization. Specify a value from `0.1` to `0.90`. You can only configure up to two digits after the decimal point.
    * CONCURRENCY_TARGET: the target for concurrency utilization. Specify a value from `0.1` to `0.95`. You can only configure up to two digits after the decimal point.



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. To update the target CPU and concurrency utilization, add the `run.googleapis.com/scaling-cpu-target` and `run.googleapis.com/scaling-concurrency-target` attributes:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/scaling-cpu-target: 'CPU_TARGET'
                 run.googleapis.com/scaling-concurrency-target: 'CONCURRENCY_TARGET'

Replace the following:

     * SERVICE: the name of your service.
     * CPU_TARGET: the target for CPU utilization. Specify a value from `0.1` to `0.90`. You can only configure up to two digits after the decimal point.
     * CONCURRENCY_TARGET: the target for concurrency utilization. Specify a value from `0.1` to `0.95`. You can only configure up to two digits after the decimal point.
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "REGION"
    
      template {
        scaling {
          cpu_utilization         = CPU_TARGET
          concurrency_utilization = CONCURRENCY_TARGET
        }
        containers {
          image = "IMAGE_URL"
        }
      }
    }
    

Replace the following:

  * SERVICE: the name of your service.
  * REGION: the Google Cloud region, for example, `europe-west1`.
  * CPU_TARGET: the target for CPU utilization. Specify a value from `0.1` to `0.90`. You can only configure up to two digits after the decimal point.
  * CONCURRENCY_TARGET: the target for concurrency utilization. Specify a value from `0.1` to `0.95`. You can only configure up to two digits after the decimal point.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`



## Disable scaling controls

You can disable either CPU utilization or concurrency utilization targets, but not both. One scaling driver must always be active. To opt out of scaling controls, restore the default utilization values instead of disabling them. When you disable a scaling driver, Cloud Run ignores that metric while making scaling decisions.

You can disable scaling controls using the Google Cloud console, gcloud CLI, YAML, or Terraform when you [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision).

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service to open its **Service details** page, then click the **Scaling** tab.

  3. Locate the **Service scaling** section. Make sure **Auto scaling** is selected. Expand the **Customize autoscaling factors** section:

     * To scale only by CPU, click the delete icon next to **Concurrent request utilization** , and enter a value for target CPU utilization if it's missing.

     * To scale only by concurrency, click the delete icon next to **CPU utilization** , and enter a value for target concurrency utilization if it's missing.

     * Click **Done** under each utilization configuration.

  4. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can disable either the [target CPU utilization](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--scaling-cpu-target) or the [target concurrency utilization](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--scaling-concurrency-target) by running the `gcloud run services update` command.

  * To scale only by CPU, disable the concurrency target by running the following command:
        
        gcloud run services update SERVICE --scaling-concurrency-target=disabled

Replace SERVICE with the name of your service.

  * To scale only by concurrency, disable the CPU target by running the following command:
        
        gcloud run services update SERVICE --scaling-cpu-target=disabled

Replace SERVICE with the name of your service.




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. To scale only by CPU, disable the concurrency target by setting the `run.googleapis.com/scaling-concurrency-target` attribute to `disabled`:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/scaling-concurrency-target: disabled

Replace SERVICE with the name of your service.

  3. To scale only by concurrency, disable the CPU target by setting the `run.googleapis.com/scaling-cpu-target` attribute to `disabled`:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/scaling-cpu-target: disabled

Replace SERVICE with the name of your service.

  4. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  


  * To scale only by CPU, disable the concurrency target by setting `concurrency_utilization` to `0`:
        
        resource "google_cloud_run_v2_service" "default" {
          name     = "SERVICE"
          location = "REGION"
        
          template {
            scaling {
              cpu_utilization         = CPU_TARGET
              concurrency_utilization = 0
            }
            containers {
              image = "IMAGE_URL"
            }
          }
        }
        

Replace the following:

    * SERVICE: the name of your service.
    * REGION: the Google Cloud region, for example, `europe-west1`.
    * CPU_TARGET: the target for CPU utilization. Specify a value from `0.1` to `0.90`. You can only configure up to two digits after the decimal point.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`
  * To scale only by concurrency, disable the CPU target by setting `cpu_utilization` to `0`:
        
        resource "google_cloud_run_v2_service" "default" {
          name     = "SERVICE"
          location = "REGION"
        
          template {
            scaling {
              cpu_utilization         = 0
              concurrency_utilization = CONCURRENCY_TARGET
            }
            containers {
              image = "IMAGE_URL"
            }
          }
        }
        

Replace the following:

    * SERVICE: the name of your service.
    * REGION: the Google Cloud region, for example, `europe-west1`.
    * CONCURRENCY_TARGET: the target for concurrency utilization. Specify a value from `0.1` to `0.95`. You can only configure up to two digits after the decimal point.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`



## Restore to default values

When you restore the target CPU or the target concurrency utilization values to default, Cloud Run uses the default utilization target of 60% instead of your custom targets. You can restore scaling controls to default using the Google Cloud console, gcloud CLI, YAML, or Terraform when you [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision).

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service to open its **Service details** page, then click the **Scaling** tab.

  3. Locate the **Service scaling** section. Make sure **Auto scaling** is selected. Expand the **Customize autoscaling factors** section to configure the following utilization targets:

     * If the **CPU utilization** and **Concurrent request utilization** targets were removed, click **Add a signal** to add each back.

     * Set the values for **CPU utilization** and **Concurrent request utilization** to `60`.

     * Click **Done** under each utilization configuration.

  4. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

Restore the [target CPU utilization](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--scaling-cpu-target) and the [target concurrency utilization](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update#--scaling-concurrency-target) to their defaults by running the `gcloud run services update` command.

  * To restore the target CPU utilization to its default value, run the following command:
        
        gcloud run services update SERVICE --scaling-cpu-target=default

Replace SERVICE with the name of your service.

  * To restore the target concurrency utilization to its default value, run the following command:
        
        gcloud run services update SERVICE --scaling-concurrency-target=default

Replace SERVICE with the name of your service.

  * To restore both the target CPU utilization and the target concurrency to their default values, run the following command:
        
        gcloud run services update SERVICE --scaling-cpu-target=default \
        --scaling-concurrency-target=default

Replace SERVICE with the name of your service.




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. To restore CPU and concurrency utilization to their default targets, **remove** the `run.googleapis.com/scaling-cpu-target` and `run.googleapis.com/scaling-concurrency-target` attributes from your YAML file:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               # Remove the scaling target annotations to restore defaults
             ...

Replace SERVICE with the name of your service.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  


To restore CPU and concurrency utilization to their default targets, **remove** the `cpu_utilization` and `concurrency_utilization` attributes from the `scaling` block in your Terraform configuration:
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "REGION"
    
      template {
        scaling {
          # Remove the scaling target attributes to restore defaults
        }
        containers {
          image = "IMAGE_URL"
        }
      }
    }
    

Replace the following:

  * SERVICE: the name of your service.
  * REGION: the Google Cloud region, for example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`



## View scaling configuration

You can view your scaling configuration using the Google Cloud console or gcloud CLI.

###  Console 

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click your service to open the **Service details** panel.

  3. Click the **Scaling** tab to view scaling settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

Replace SERVICE with the name of your service.

  2. Locate the value for the **Target CPU utilization:** and **Target concurrency utilization:** settings in the returned configuration.




## Best practices

You can optimize costs and prevent overscaling by decreasing the number of instances, or you can improve performance by scaling more aggressively in response to specific drivers. To determine the optimal utilization targets for your workload, use the following strategies:

  * Before adjusting targets, identify which metric is triggering your service to scale. Follow these steps to identify the scaling metric:

    1. Go to [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in the Google Cloud console to review the monitoring chart for your scaling driver.

    2. Search and select the `run.googleapis.com/scaling/recommended_instances` metric, and set **Aggregation** to **Unaggregated** to view the metric grouped by scaling driver.

The driver with the highest value is the one controlling your service's instance count. If you want a different driver to take priority, or if you want to scale more or less aggressively, adjust the utilization target for that specific driver.

If Adaptive Concurrency Tuning (ACT) is the scaling driver, it indicates that 1-second CPU utilization is exceeding 90% for individual instances and Cloud Run is dynamically limiting request concurrency to protect your service. To mitigate ACT driving your scaling, consider increasing the CPU allocation or adjusting your concurrency settings. For more information, see [About instance autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling#adaptive-concurrency).

  * Adjust targets incrementally, and wait for a few minutes between adjustments to observe the effect on performance.

  * Use [traffic splitting](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) to test new scaling targets by directing a small percentage of your traffic to a separate revision before rolling them out to your entire service.




### About low utilization targets

Lowering your utilization target to the minimum of `0.1` (10%) significantly changes how your service scales.

Benefits of setting a low utilization target include:

  * **High service availability** : Your service scales up much earlier, maintaining a large buffer of idle capacity to handle sudden traffic spikes without latency hits.

  * **Faster scaling at low instance counts** : Services scale more reliably before hitting high-utilization bottlenecks.




Drawbacks of setting low utilization targets include:

  * **Potential for cost increase** : You run more instances than strictly necessary for your current load, leading to higher billing.
  * **More frequent scaling decisions** : At lower utilizations, Cloud Run has a lower tolerance, and doesn't wait as long before scaling.

**Note:** Inversely, if you set a high target utilization value, Cloud Run has higher tolerance, and waits longer before scaling. For example, a 10% tolerance on a `0.8` target creates a wide target range from `0.72` to `0.88` where no scaling occurs. Because of this wider window, when your instances scale, you might see an all-at-once scaling behavior instead of a smooth curve. For more information about how Cloud Run applies the tolerance and calculates the number of instances, see [About instance autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling#scale-up).

## What's next

  * To learn more about autoscaling concepts and behaviors, see [About instance autoscaling in Cloud Run services](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).
  * To learn about other scaling options, see [manual scaling](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling).
  * To manage the maximum number of instances of your Cloud Run services, see [Setting a maximum number of instances](https://docs.cloud.google.com/run/docs/configuring/max-instances).
  * To manage the maximum number of simultaneous requests handled by each instance, see [Setting concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency).
  * To optimize your concurrency setting, see [development tips for tuning concurrency](https://docs.cloud.google.com/run/docs/tips#tuning-concurrency).
  * To specify an idle instance to keep running to minimize latency or cold starts on first requests, see [Using `min-instance` to enable idle instances](https://docs.cloud.google.com/run/docs/configuring/min-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
