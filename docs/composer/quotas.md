---
url: https://docs.cloud.google.com/composer/quotas/
title: Quotas and limits \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:12.215083+00:00
---

# Quotas and limits  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/quotas/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Resources ](https://docs.cloud.google.com/composer/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Managed Service for Apache Airflow.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Managed Airflow resources. System limits can't be changed. 

## Managed Airflow quotas

Quotas in this section apply only to Cloud Composer API and tools that utilize Cloud Composer API:

  * Managed Airflow interface in Google Cloud console
  * `gcloud composer` and `gcloud beta composer` commands
  * Managed Airflow REST API
  * Managed Airflow RPC API
  * Terraform, for operations with Managed Airflow environments



Quotas in this section do not apply to any services that you use in your Airflow DAGs. Such services use their own quotas.

Managed Airflow has the following API quotas:

Quota name | Limit  
---|---  
Read requests per project | 1,000 quota units per minute  
Write requests per project | 25,000 quota units per day  
Write requests per project | 1,500 quota units per minute  
Save snapshot requests per project | 5,000 quota units per day  
Save snapshot requests per project | 250 quota units per minute  
Save snapshot requests per project per environment | 2,600 quota units per day   
Load snapshot requests per project | 2,500 quota units per day  
Load snapshot requests per project | 150 quota per minute  
Load snapshot requests per project per environment | 700 quota units per day   
  
Cloud Composer API calls have the following costs, in quota units:

Operation | Cost in quota units | Request type  
---|---|---  
All operations | 1 | Read  
environments.create | 100 | Write  
environments.patch | 100 | Write  
environments.delete | 100 | Write  
environments.databaseFailover | 100 | Write  
environments.restartWebServer | 100 | Write  
environments.checkUpgrade | 100 | Write  
environments.executeAirflowCommand | 25 | Write  
environments.stopAirflowCommand | 25 | Write  
environments.saveSnapshot | 50 | Save snapshot  
environments.loadSnapshot | 50 | Load snapshot  
  
## Quota calculation examples

  * One `environments.create` request consumes 100 quota units from the **Write** quotas.

There are two such quotas for write requests:

    * **Write requests per project per day**
    * **Write requests per project per minute**

This operation consumes 100 quota units from each quota.

If you execute an `environments.restartWebServer` request afterwards, another 100 quota units are consumed from the same quotas, because `environments.restartWebServer` shares quotas with the `environments.create` request.

  * One `environments.saveSnapshot` request consumes 50 quota units from three quotas:

    * **Save snapshot requests per project per day**
    * **Save snapshot requests per project per minute**
    * **Save snapshot requests per project per environment per day**

These three quotas limit the maximum number of `environments.saveSnapshot` requests. Each does it in a different way.

The **Save snapshot requests per project per day** quota limit is 2500 quota units. You can execute up to 50 `environments.saveSnapshot` requests in your project every day.

The **Save snapshot requests per project per minute** quota limit is 150 quota units. In one minute, you can execute only up to three `environments.saveSnapshot` requests in your project.

Finally, the **Save snapshot requests per project per environment per day** quota limit is 750 quota units. You can execute up to 15 `environments.saveSnapshot` requests every day for a single environment. If all quota units are consumed for a specific environment, you can still run `environments.saveSnapshot` requests for other environments in your project.




## Resource and instance quotas

The following quotas apply to resources and instances utilized by a Managed Airflow environment:

Version | Resource | Quota limit  
---|---|---  
Managed Airflow (Gen 3) | Total number of vCPUs utilized by all environment components | 250 vCPU  
Managed Airflow (Gen 3) | Total number of active KubernetesPodOperator and Kubertenes Executor instances | 50 instances  
**Note:** To request a limit increase for your environment, contact [Cloud Customer Care](https://docs.cloud.google.com/support).

## Quotas for other services

Managed Airflow uses other Google Cloud services. These services have project-level quotas, which apply when you use Managed Airflow.

For example, quotas for Cloud Storage apply to all buckets associated with environments in your project. As another example, environment's clusters use Google Kubernetes Engine, so quotas for GKE apply to all clusters associated with environments in your project.

### Quotas for services used by Managed Airflow

The following services are used by Managed Airflow. These services have their own quota limits:

  * [Cloud Deployment Manager quotas](https://docs.cloud.google.com/deployment-manager/quotas)
  * [Google Kubernetes Engine quotas](https://docs.cloud.google.com/kubernetes-engine/quotas)
  * [Compute Engine quotas](https://docs.cloud.google.com/compute/quotas)
  * [Cloud Storage quotas](https://docs.cloud.google.com/storage/quotas)
  * [Pub/Sub quotas](https://docs.cloud.google.com/pubsub/quotas)
  * [Cloud Logging quotas](https://docs.cloud.google.com/logging/quotas)
  * [Cloud Monitoring quotas](https://docs.cloud.google.com/monitoring/quotas)
  * [Cloud Build quotas](https://docs.cloud.google.com/build/quotas) (apply to environments that use custom PyPI packages)
  * [Artifact Registry quotas](https://docs.cloud.google.com/artifact-registry/quotas)
  * [Identity and Access Management quotas](https://docs.cloud.google.com/iam/quotas)
  * [Virtual Private Cloud quotas](https://docs.cloud.google.com/vpc/docs/quota) (does not apply to environments that use Private Service Connect)
  * [Resource Manager quotas](https://docs.cloud.google.com/resource-manager/docs/limits)
  * [Service Directory quotas](https://docs.cloud.google.com/service-directory/quotas)



## Quotas for optional services

You can use [Airflow operators](https://airflow.apache.org/docs/apache-airflow/stable/concepts/operators.html) with Google Cloud services. Any service that you use in a DAG is subject to that service's quotas.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
