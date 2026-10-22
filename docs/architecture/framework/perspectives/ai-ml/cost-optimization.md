---
url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization/
title: AI and ML perspective: Cost optimization \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:03:04.686383+00:00
---

# AI and ML perspective: Cost optimization  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  AI and ML perspective: Cost optimization Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-28 UTC

This document in [Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) provides an overview of principles and recommendations to optimize the cost of your AI systems throughout the ML lifecycle. By adopting a proactive and informed cost management approach, your organization can realize the full potential of AI and ML systems and also maintain financial discipline. The recommendations in this document align with the [cost optimization pillar](https://docs.cloud.google.com/architecture/framework/cost-optimization) of the Google Cloud Well-Architected Framework.

AI and ML systems can help you unlock valuable insights and predictive capabilities from data. For example, you can reduce friction in internal processes, improve user experiences, and gain deeper customer insights. The cloud offers vast amounts of resources and quick time-to-value without large up-front investments for AI and ML workloads. To maximize business value and to align the spending with your business goals, you need to understand the cost drivers, proactively optimize costs, set up spending controls, and adopt [FinOps](https://cloud.google.com/learn/what-is-finops) practices.

The recommendations in this document are mapped to the following core principles:

  * [Define and measure costs and returns](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#define_and_measure_costs_and_returns)
  * [Optimize resource allocation](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#optimize_resource_allocation)
  * [Enforce data management and governance practices](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#enforce_data_management_and_governance_practices)
  * [Automate and streamline with MLOps](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#automate_and_streamline_with_mlops)
  * [Use managed services and pre-trained models](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#use_managed_services_and_pre-trained_models)



## Define and measure costs and returns

To effectively manage AI and ML costs in Google Cloud, you must define and measure the cloud resource costs and the business value of your AI and ML initiatives. To help you track expenses granularly, Google Cloud provides comprehensive billing and cost management tools, such as the following:

  * Cloud Billing reports and tables
  * Data Studio dashboards, budgets, and alerts
  * Cloud Monitoring
  * Cloud Logging



To make informed decisions about resource allocation and optimization, consider the following recommendations.

### Establish business goals and KPIs

Align the technical choices in your AI and ML projects with business goals and key performance indicators (KPIs).

#### Define strategic objectives and ROI-focused KPIs

Ensure that AI and ML projects are aligned with strategic objectives like revenue growth, cost reduction, customer satisfaction, and efficiency. Engage stakeholders to understand the business priorities. Define AI and ML objectives that are specific, measurable, attainable, relevant, and time-bound (SMART). For example, a SMART objective is: "Reduce chat handling time for customer support by 15% in 6 months by using an AI chatbot".

To make progress towards your business goals and to measure the return on investment (ROI), define KPIs for the following categories of metrics:

  * Costs for training, inference, storage, and network resources, including specific unit costs (such as the cost per inference, data point, or task). These metrics help you gain insights into efficiency and cost optimization opportunities. You can track these costs by using [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports) and [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards).
  * Business value metrics like revenue growth, cost savings, customer satisfaction, efficiency, accuracy, and adoption. You can track these metrics by using [BigQuery analytics](https://docs.cloud.google.com/bigquery/docs/query-overview) and [Looker dashboards](https://docs.cloud.google.com/looker/docs/dashboards).
  * Industry-specific metrics like the following:

    * Retail industry: measure revenue lift and churn
    * Healthcare industry: measure patient time and patient outcomes
    * Finance industry: measure fraud reduction
  * Project-specific metrics. You can track these metrics by using [Experiments on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments) and [evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction).

    * Predictive AI: measure accuracy and precision
    * Generative AI: measure adoption, satisfaction, and content quality
    * Computer vision AI: measure accuracy



#### Foster a culture of cost awareness and continuous optimization

Adopt [FinOps](https://cloud.google.com/learn/what-is-finops) principles to ensure that each AI and ML project has estimated costs and has ways to measure and track actual costs throughout its lifecycle. Ensure that the costs and business benefits of your projects have assigned owners and clear accountability.

For more information, see [Foster a culture of cost awareness](https://docs.cloud.google.com/architecture/framework/cost-optimization/foster-culture-cost-awareness) in the Cost Optimization pillar of the Google Cloud Well-Architected Framework.

#### Drive value and continuous optimization through iteration and feedback

Map your AI and ML applications directly to your business goals and measure the ROI.

To validate your ROI hypotheses, start with pilot projects and use the following iterative optimization cycle:

  1. **Monitor continuously and analyze data** : Monitor KPIs and costs to identify deviations and opportunities for optimization.
  2. **Make data-driven adjustments** : Optimize strategies, models, infrastructure, and resource allocation based on data insights.
  3. **Refine iteratively** : Adapt business objectives and KPIs based on the things you learned and the evolving business needs. This iteration helps you maintain relevance and strategic alignment.
  4. **Establish a feedback loop** : Review performance, costs, and value with stakeholders to inform ongoing optimization and future project planning.



### Manage billing data with Cloud Billing and labels

Effective cost optimization requires visibility into the source of each cost element. The recommendations in this section can help you use Google Cloud tools to get granular insights into your AI and ML costs. You can also attribute costs to specific AI and ML projects, teams, and activities. These insights lay the groundwork for cost optimization.

#### Organize and label Google Cloud resources

  * Structure your projects and resources in a hierarchy that reflects your organizational structure and your AI and ML workflows. To track and analyze costs at different levels, organize your Google Cloud resources by using organizations, folders, and projects. For more information, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).
  * Apply meaningful [labels](https://docs.cloud.google.com/resource-manager/docs/labels-overview) to your resources. You can use labels that indicate the project, team, environment, model name, dataset, use case, and performance requirements. Labels provide valuable context for your billing data and enable granular cost analysis.
  * Maintain consistency in your labeling conventions across all of your AI and ML projects. Consistent labeling conventions ensure that your billing data is organized and can be readily analyzed.



#### Use billing-related tools

  * To facilitate detailed analysis and reporting, [export the billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). BigQuery has powerful query capabilities that let you analyze the billing data to help you understand your costs.
  * To aggregate costs by labels, projects, or specific time periods, you can write custom SQL queries in BigQuery. Such queries let you attribute costs to specific AI and ML activities, such as model training, hyperparameter tuning, or inference.
  * To identify cost anomalies or unexpected spending spikes, use the analytic capabilities in BigQuery. This approach can help you detect potential issues or inefficiencies in your AI and ML workloads.
  * To identify and manage unexpected costs, use the [anomaly detection dashboard](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies) in Cloud Billing.
  * To distribute costs across different teams or departments based on resource usage, use Google Cloud's [cost allocation](https://services.google.com/fh/files/misc/cloud_finops_shared_services_cost_allocation_whitepaper.pdf) feature. Cost allocation promotes accountability and transparency.
  * To gain insights into spending patterns, explore the prebuilt [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports). You can filter and customize these reports to focus on specific AI and ML projects or services.



### Monitor resources continuously with dashboards, alerts, and reports

To create a scalable and resilient way to track costs, you need continuous monitoring and reporting. Dashboards, alerts, and reports constitute the foundation for effective cost tracking. This foundation lets you maintain constant access to cost information, identify areas of optimization, and ensure alignment between business goals and costs.

#### Create a reporting system

Create scheduled reports and share them with appropriate stakeholders.

Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to collect metrics from various sources, including your applications, infrastructure, and Google Cloud services like Compute Engine, Google Kubernetes Engine (GKE), and Cloud Run functions. To visualize metrics and logs in real time, you can use the prebuilt Cloud Monitoring dashboard or create custom dashboards. Custom dashboards let you define and add metrics to track specific aspects of your systems, like model performance, API calls, or business-level KPIs.

Use [Cloud Logging](https://docs.cloud.google.com/logging/docs) for centralized collection and storage of logs from your applications, systems, and Google Cloud services. Use the logs for the following purposes:

  * Track costs and utilization of resources like CPU, memory, storage, and network.
  * Identify cases of over-provisioning (where resources aren't fully utilized) and under-provisioning (where there are insufficient resources). Over-provisioning results in unnecessary costs. Under-provisioning slows training times and might cause performance issues.
  * Identify idle or underutilized resources, such as VMs and GPUs, and take steps to shut down or rightsize them to optimize costs.
  * Identify cost spikes to detect sudden and unexpected increases in resource usage or costs.



Use [Looker](https://docs.cloud.google.com/looker/docs/intro) or [Data Studio](https://docs.cloud.google.com/looker/docs/studio) to create interactive dashboards and reports. Connect the dashboards and reports to various data sources, including BigQuery and Cloud Monitoring.

#### Set alert thresholds based on key KPIs

For your KPIs, determine the thresholds that should trigger alerts. Meaningful alert thresholds can help you avoid alert fatigue. Create [alerting policies](https://docs.cloud.google.com/monitoring/alerts) in Cloud Monitoring to get notifications related to your KPIs. For example, you can get notifications when accuracy drops below a certain threshold or latency exceeds a defined limit. Alerts based on log data can notify you about potential cost issues in real time. Such alerts let you take corrective actions promptly and prevent further financial loss.

## Optimize resource allocation

To achieve cost efficiency for your AI and ML workloads in Google Cloud, you must optimize resource allocation. To help you avoid unnecessary expenses and ensure that your workloads have the resources that they need to perform optimally, align resource allocation with the needs of your workloads.

To optimize the allocation of cloud resources to AI and ML workloads, consider the following recommendations.

### Use autoscaling to dynamically adjust resources

Use Google Cloud services that support autoscaling, which automatically adjusts resource allocation to match the current demand. Autoscaling provides the following benefits:

  * **Cost and performance optimization** : You avoid paying for idle resources. At the same time, autoscaling ensures that your systems have the necessary resources to perform optimally, even at peak load.
  * **Improved efficiency** : You free up your team to focus on other tasks.
  * **Increased agility** : You can respond quickly to changing demands and maintain high availability for your applications.



The following table summarizes the techniques that you can use to implement autoscaling for different stages of your AI projects.

Stage | Autoscaling techniques  
---|---  
Training | 

  * Use managed services like [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview) or [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), which offer built-in autoscaling capabilities for training jobs.
  * Configure autoscaling policies to scale the number of training instances based on metrics like CPU utilization, memory usage, and job queue length.
  * Use custom scaling metrics to fine-tune autoscaling behavior for your specific workloads.

  
Inference | 

  * Deploy your models on scalable platforms like [Gemini Enterprise Agent Platform Inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/overview), [GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling), or [TPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu). 
  * Use autoscaling features to adjust the number of replicas based on metrics like request rate, latency, and resource utilization.
  * Implement load balancing to distribute traffic evenly across replicas and ensure high availability.

  
  
### Start with small models and datasets

To help reduce costs, test ML hypotheses at a small scale when possible and use an iterative approach. This approach, with smaller models and datasets, provides the following benefits:

  * **Reduced costs from the start** : Less compute power, storage, and processing time can result in lower costs during the initial experimentation and development phases.
  * **Faster iteration** : Less training time is required, which lets you iterate faster, explore alternative approaches, and identify promising directions more efficiently.
  * **Reduced complexity** : Simpler debugging, analysis, and interpretation of results, which leads to faster development cycles.
  * **Efficient resource utilization** : Reduced chance of over-provisioning resources. You provision only the resources that are necessary for the current workload.



Consider the following recommendations:

  * **Use sample data first** : Train your models on a representative subset of your data. This approach lets you assess the model's performance and identify potential issues without processing the entire dataset.
  * **Experiment by using notebooks** : Start with smaller instances and scale as needed. You can use [Gemini Enterprise Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction), a managed Jupyter notebook environment that's well suited for experimentation with different model architectures and datasets.
  * **Start with simpler or pre-trained models** : Use [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) to discover and explore the pre-trained models. Such models require fewer computational resources. Gradually increase the complexity as needed based on performance requirements.

    * Use pre-trained models for tasks like image classification and natural language processing. To save on training costs, you can fine-tune the models on smaller datasets initially.
    * Use [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) for structured data. BigQuery ML lets you create and deploy models directly within BigQuery. This approach can be cost-effective for initial experimentation, because you can take advantage of the pay-per-query pricing model for BigQuery.
  * **Scale for resource optimization** : Use Google Cloud's flexible infrastructure to scale resources as needed. Start with smaller instances and adjust their size or number when necessary.




### Discover resource requirements through experimentation

Resource requirements for AI and ML workloads can vary significantly. To optimize resource allocation and costs, you must understand the specific needs of your workloads through systematic experimentation. To identify the most efficient configuration for your models, test different configurations and analyze their performance. Then, based on the requirements, right-size the resources that you used for training and serving.

We recommend the following approach for experimentation:

  1. **Start with a baseline** : Begin with a baseline configuration based on your initial estimates of the workload requirements. To create a baseline, you can use the [Pricing Calculator](https://cloud.google.com/products/calculator) for new workloads or use an existing [billing report](https://docs.cloud.google.com/billing/docs/how-to/reports).
  2. **Understand your quotas** : Before launching extensive experiments, familiarize yourself with your Google Cloud project [quotas](https://docs.cloud.google.com/docs/quotas/overview) for the resources and APIs that you plan to use. The quotas determine the range of configurations that you can realistically test. By becoming familiar with quotas, you can work within the available resource limits during the experimentation phase.
  3. **Experiment systematically** : Adjust parameters like the number of CPUs, amount of memory, number and type of GPUs and TPUs, and storage capacity. [Gemini Enterprise Agent Platform Managed Training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview) and [Agent Platform Inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/overview) let you experiment with different machine types and configurations.
  4. **Monitor utilization, cost, and performance** : Track the resource utilization, cost, and key performance metrics such as training time, inference latency, and model accuracy, for each configuration that you experiment with.

     * To track resource utilization and performance metrics, you can use the Agent Platform console.
     * To collect and analyze detailed performance metrics, use Cloud Monitoring.
     * To view costs, use [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports) and [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards).
     * To identify performance bottlenecks in your models and optimize resource utilization, use profiling tools like [Agent Platform TensorBoard](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-introduction).
  5. **Analyze costs** : Compare the cost and performance of each configuration to identify the most cost-effective option.

  6. **Establish resource thresholds and improvement targets based on quotas** : Define thresholds for when scaling begins to yield diminishing returns in performance, such as minimal reduction in training time or latency for a significant cost increase. Consider project quotas when setting these thresholds. Determine the point where the cost and potential quota implications of further scaling are no longer justified by performance gains.

  7. **Refine iteratively** : Repeat the experimentation process with refined configurations based on your findings. Always ensure that the resource usage remains within your allocated quotas and aligns with established cost-benefit thresholds.




### Use MLOps to reduce inefficiencies

As organizations increasingly use ML to drive innovation and efficiency, managing the ML lifecycle effectively becomes critical. ML operations (MLOps) is a set of practices that automate and streamline the ML lifecycle, from model development to deployment and monitoring.

#### Align MLOps with cost drivers

To take advantage of MLOps for cost efficiency, identify the primary cost drivers in the ML lifecycle. Then, you can adopt and implement MLOps practices that are aligned with the cost drivers. Prioritize and adopt the MLOps features that address the most impactful cost drivers. This approach helps ensure a manageable and successful path to significant cost savings.

#### Implement MLOps for cost optimization

The following are common MLOps practices that help to reduce cost:

  * **Version control** : Tools like Git can help you to track versions of code, data, and models. Version control ensures reproducibility, facilitates collaboration, and prevents costly rework that can be caused by versioning issues.
  * **Continuous integration and continuous delivery (CI/CD)** : [Cloud Build](https://docs.cloud.google.com/build/docs/overview) and [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) let you implement CI/CD pipelines to automate building, testing, and deployment of your ML models. CI/CD pipelines ensure efficient resource utilization and minimize the costs associated with manual interventions.
  * **Observability** : [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) let you track model performance in production, identify issues, and trigger alerts for proactive intervention. Observability lets you maintain model accuracy, optimize resource allocation, and prevent costly downtime or performance degradation.
  * **Model retraining** : [Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) simplifies the processes for retraining models periodically or when performance degrades. When you use Agent Platform Pipelines for retraining, it helps ensure that your models remain accurate and efficient, which can prevent unnecessary resource consumption and maintain optimal performance.
  * **Automated testing and evaluation** : [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction) helps you accelerate and standardize model evaluation. Implement automated tests throughout the ML lifecycle to ensure the quality and reliability of your models. Such tests can help you catch errors early, prevent costly issues in production, and reduce the need for extensive manual testing.



For more information, see [MLOps: Continuous delivery and automation pipelines in machine learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

## Enforce data management and governance practices

Effective data management and governance practices are critical to cost optimization. Well organized data can encourage teams to reuse datasets, avoid needless duplication, and reduce the effort to obtain high quality data. By proactively managing data, you can reduce storage costs, enhance data quality, and ensure that your ML models are trained on the most relevant and valuable data.

To implement data management and governance practices, consider the following recommendations.

### Establish and adopt a data governance framework

The growing prominence of AI and ML has made data the most valuable asset for organizations that are undergoing digital transformation. A robust framework for [data governance](https://cloud.google.com/learn/what-is-data-governance) is a crucial requirement for managing AI and ML workloads cost-effectively at scale. A data governance framework with clearly defined policies, procedures, and roles provides a structured approach for managing data throughout its lifecycle. Such a framework helps to improve data quality, enhance security, improve utilization, and reduce redundancy.

#### Establish a data governance framework

There are many pre-existing frameworks for data governance, such as the frameworks published by the [EDM Council](https://edmcouncil.org/), with options available for different industries and organization sizes. Choose and adapt a framework that aligns with your specific needs and priorities.

#### Implement the data governance framework

Google Cloud provides the following services and tools to help you implement a robust data governance framework:

  * [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) is an intelligent data fabric that helps you unify distributed data and automate data governance without the need to consolidate data sets in one place. This helps to reduce the cost to distribute and maintain data, facilitate data discovery, and promote reuse.

    * To organize data, use Knowledge Catalog abstractions and set up [logical data lakes and zones](https://docs.cloud.google.com/dataplex/docs/create-lake).
    * To administer access to data lakes and zones, use [Google Groups](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console) and [Knowledge Catalog roles](https://docs.cloud.google.com/dataplex/docs/lake-security).
    * To streamline data quality processes, enable [auto data quality](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview).
  * Knowledge Catalog is also a fully managed and scalable metadata management service. The [catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview) provides a foundation that ensures that data assets are accessible and reusable.

    * Metadata from the [supported Google Cloud sources](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources) is automatically ingested into the universal catalog. For data sources outside of Google Cloud, [create custom entries](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#create-custom-entry).
    * To improve the discoverability and management of data assets, enrich technical metadata with business metadata by using [aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#aspects).
    * Ensure that data scientists and ML practitioners have sufficient [permissions](https://docs.cloud.google.com/dataplex/docs/iam-permissions) to access Knowledge Catalog and use the [search](https://docs.cloud.google.com/dataplex/docs/search-assets) function.
  * [BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction) lets you efficiently and securely exchange data assets across your organizations to address challenges of data reliability and cost.

    * Set up [data exchanges](https://docs.cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges) and ensure that curated data assets can be viewed as [listings](https://docs.cloud.google.com/bigquery/docs/analytics-hub-manage-listings).
    * Use [data clean rooms](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms) to securely manage access to sensitive data and efficiently partner with external teams and organizations on AI and ML projects.
    * Ensure that data scientists and ML practitioners have sufficient [permissions](https://docs.cloud.google.com/bigquery/docs/analytics-hub-grant-roles) to view and publish datasets to BigQuery sharing.



### Make datasets and features reusable throughout the ML lifecycle

For significant efficiency and cost benefits, reuse datasets and features across multiple ML projects. When you avoid redundant data engineering and feature development efforts, your organization can accelerate model development, reduce infrastructure costs, and free up valuable resources for other critical tasks.

Google Cloud provides the following services and tools to help you reuse datasets and features:

  * Data and ML practitioners can publish [data products](https://docs.cloud.google.com/architecture/build-data-products-data-mesh) to maximize reuse across teams. The data products can then be discovered and used through Knowledge Catalog and BigQuery sharing.
  * For tabular and structured datasets, you can use [Agent Platform Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) to promote reusability and streamline feature management through BigQuery.
  * You can store unstructured data in Cloud Storage and govern the data by using [BigQuery object tables and signed URLs](https://docs.cloud.google.com/bigquery/docs/object-table-introduction).
  * You can manage vector embeddings by including metadata in your [Vector Search indexes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/create-manage-index).



## Automate and streamline with MLOps

A primary benefit of adopting MLOps practices is a reduction in costs for technology and personnel. Automation helps you avoid the duplication of ML activities and reduce the workload for data scientists and ML engineers.

To automate and streamline ML development with MLOps, consider the following recommendations.

### Automate and standardize data collection and processing

To help reduce ML development effort and time, automate and standardize your data collection and processing technologies.

#### Automate data collection and processing

This section summarizes the products, tools, and techniques that you can use to automate data collection and processing.

Identify and choose the relevant data sources for your AI and ML tasks:

  * Database options such as [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction), [Spanner](https://docs.cloud.google.com/spanner), [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview), [Firestore](https://docs.cloud.google.com/firestore/native/docs), and [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction). Your choice depends on your requirements, such as latency on write access (static or dynamic), data volume (high or low), and data format (structured, unstructured, or semi-structured). For more information, see [Google Cloud databases](https://cloud.google.com/products/databases#our-portfolio-of-databases).
  * Data lakes such as Cloud Storage with [BigLake](https://docs.cloud.google.com/bigquery/docs/biglake-intro).
  * [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) for governing data across sources.
  * Streaming events platforms such as [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview), or [Apache Kafka](https://kafka.apache.org/).
  * External APIs.



For each of your data sources, choose an ingestion tool:

  * Dataflow: For batch and stream processing of data from various sources, with ML-component integration. For an event-driven architecture, you can combine Dataflow with [Eventarc](https://docs.cloud.google.com/eventarc/docs) to efficiently process data for ML. To enhance MLOps and ML job efficiency, use GPU and right-fitting capabilities.
  * [Cloud Run functions](https://docs.cloud.google.com/run/docs/resource-model#functions): For event-driven data ingestion that gets triggered by changes in data sources for real-time applications.
  * BigQuery: For classical tabular data ingestion with frequent access.



Choose tools for data transformation and loading:

  * Use tools such as [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) or [Dataform](https://docs.cloud.google.com/dataform/docs/overview) to automate data transformations like feature scaling, encoding categorical variables, and creating new features in batch, streaming, or real time. The tools that you select depend upon your requirements and chosen services.
  * Use [Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) to automate feature creation and management. You can centralize features for reuse across different models and projects.



#### Standardize data collection and processing

To discover, understand, and manage data assets, use metadata management services like [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview). It helps you standardize data definitions and ensure consistency across your organization.

To enforce standardization and avoid the cost of maintaining multiple custom implementations, use automated training pipelines and orchestration. For more information, see the next section.

### Automate training pipelines and reuse existing assets

To boost efficiency and productivity in MLOps, automated training pipelines are crucial. Google Cloud offers a robust set of tools and services to build and deploy training pipelines, with a strong emphasis on reusing existing assets. Automated training pipelines help to accelerate model development, ensure consistency, and reduce redundant effort.

#### Automate training pipelines

The following table describes the Google Cloud services and features that you can use to automate the different functions of a training pipeline.

Function | Google Cloud services and features  
---|---  
Orchestration: Define complex ML workflows consisting of multiple steps and dependencies. You can define each step as a separate containerized task, which helps you manage and scale individual tasks with ease. | 

  * To create and orchestrate pipelines, use [Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) or Kubeflow Pipelines. These tools support simple data transformation, model training, model deployment, and pipeline versioning. They let you define dependencies between steps, manage data flow, and automate the execution of the entire workflow.
  * For complex operational tasks with heavy CI/CD and extract, transform, and load (ETL) requirements, use [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview). If you prefer Airflow for data orchestration, Managed Service for Apache Airflow is a compatible managed service that's built on Airflow.
  * For pipelines that are managed outside of Agent Platform Pipelines, use [Workflows](https://docs.cloud.google.com/workflows/docs/choose-orchestration) for infrastructure-focused tasks like starting and stopping VMs or integrating with external systems.
  * To automate your CI/CD process, use [Cloud Build](https://docs.cloud.google.com/build/docs/overview) with [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview). You can set up notifications and automatic triggers for when new code is pushed or when a new model needs to be trained.
  * For a fully-managed, scalable solution for pipeline management, use [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview). 

  
Versioning: Track and control different versions of pipelines and components to ensure reproducibility and auditability. | Store [Kubeflow pipeline](https://docs.cloud.google.com/artifact-registry/docs/kfp) templates in a Kubeflow Pipelines repository in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).  
Reusability: Reuse existing pipeline components and artifacts, such as prepared datasets and trained models, to accelerate development. | Store your pipeline templates in [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) and share them across your organization.  
Monitoring: Monitor pipeline execution to identify and address any issues. | Use Cloud Logging and Cloud Monitoring. For more information, see [Monitor resources continuously with dashboards, alerts, and reports](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#monitor_resources_continuously_with_dashboards_alerts_and_reports).  
  
#### Expand reusability beyond pipelines

Look for opportunities to expand reusability beyond training pipelines. The following are examples of Google Cloud capabilities that let you reuse ML features, datasets, models, and code.

  * [Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) provides a centralized repository for organizing, storing, and serving ML features. It lets you reuse features across different projects and models, which can improve consistency and reduce feature engineering effort. You can store, share, and access features for both online and offline use cases.
  * [Agent Platform datasets](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/overview) enable teams to create and manage datasets centrally, so your organization can maximize reusability and reduce data duplication. Your teams can search and discover the datasets by using [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).
  * [Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction) lets you store, manage, and deploy your trained models. Model Registry lets you reuse the models in subsequent pipelines or for online prediction, which helps you take advantage of previous training efforts.
  * [Custom containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/containers-overview) let you package your training code and dependencies into containers and store the containers in Artifact Registry. Custom containers let you provide consistent and reproducible training environments across different pipelines and projects.



### Use Google Cloud services for model evaluation and tuning

Google Cloud offers a powerful suite of tools and services to streamline and automate model evaluation and tuning. These tools and services can help you reduce your time to production and reduce the resources required for continuous training and monitoring. By using these services, your AI and ML teams can enhance model performance with fewer expensive iterations, achieve faster results, and minimize wasted compute resources.

#### Use resource-efficient model evaluation and experimentation

Begin an AI project with experiments before you scale up your solution. In your experiments, track various metadata such as dataset version, model parameters, and model type. For further reproducibility and comparison of the results, use metadata tracking in addition to code versioning, similar to the capabilities in Git. To avoid missing information or deploying the wrong version in production, use [Experiments on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments) before you implement full-scale deployment or training jobs.

Experiments on Agent Platform lets you do the following:

  * Streamline and automate metadata tracking and discovery through a user friendly UI and API for production-ready workloads.
  * Analyze the model's performance metrics and compare metrics across multiple models.



After the model is trained, continuously monitor the performance and data drift over time for incoming data. To streamline this process, use [Model Monitoring on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to directly access the created models in [Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). Model Monitoring on Agent Platform also automates monitoring for data and results through online and batch predictions. You can export the results to BigQuery for further analysis and tracking.

#### Choose optimal strategies to automate training

For hyperparameter tuning, we recommend the following approaches:

  * To automate the process of finding the optimal hyperparameters for your models, use [Agent Platform hyperparameter tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuning-overview). Agent Platform uses advanced algorithms to explore the hyperparameter space and identify the best configuration.
  * For efficient hyperparameter tuning, consider using [Bayesian optimization](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuning-overview#understanding-trials) techniques, especially when you deal with complex models and large datasets.



For distributed training, we recommend the following approaches:

  * For large datasets and complex models, use the distributed training infrastructure of Agent Platform. This approach lets you train your models on multiple machines, which helps to significantly reduce training time and associated costs. Use tools like the following:

    * [Agent Platform tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning) to perform supervised fine-tuning of Gemini, Imagen, and other models.
    * [Agent Platform Managed Training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview) or [Ray on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray) for custom distributed training.
  * Choose optimized ML frameworks, like Keras and PyTorch, that support distributed training and efficient resource utilization.




#### Use explainable AI

It's crucial to understand why a model makes certain decisions and to identify potential biases or areas for improvement. Use explainability techniques to gain insights into your model's predictions.

  * **Feature-based** : To understand which features are most influential in your model's predictions, analyze [feature attributions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-explanations). This understanding can guide feature-engineering efforts and improve model interpretability.
  * **Example-based** : To return a list of examples (typically from the training set) that are most similar to the input, use nearest-neighbor search. Because similar inputs generally yield similar predictions, you can use these explanations to explore and explain a model's behavior.



## Use managed services and pre-trained models

Adopt an incremental approach to model selection and model development. This approach helps you avoid excessive costs that are associated with starting afresh every time. To control costs, use ML frameworks, managed services, and pre-trained models.

To get the maximum value from managed services and pre-trained models, consider the following recommendations.

### Use notebooks for exploration and experiments

[Notebook](https://en.wikipedia.org/wiki/Notebook_interface) environments are crucial for cost-effective ML experimentation. A notebook provides an interactive and collaborative space for data scientists and engineers to explore data, develop models, share knowledge, and iterate efficiently. Collaboration and knowledge sharing through notebooks significantly accelerates development, code reviews, and knowledge transfer. Notebooks help streamline workflows and reduce duplicated effort.

Instead of procuring and managing expensive hardware for your development environment, you can use the scalable and on-demand infrastructure of Gemini Enterprise Agent Platform Workbench and Colab Enterprise.

  * [Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction) is a Jupyter notebook development environment for the entire data science workflow. You can interact with Agent Platform and other Google Cloud services from within an instance's Jupyter notebook. Agent Platform Workbench integrations and features help you do the following:

    * Access and explore data from a Jupyter notebook by using BigQuery and Cloud Storage integrations.
    * Automate recurring updates to a model by using scheduled executions of code that runs on Agent Platform.
    * Process data quickly by running a notebook on a Managed Service for Apache Spark cluster.
    * Run a notebook as a step in a pipeline by using Agent Platform Pipelines.
  * [Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction) is a collaborative, managed notebook environment that has the security and compliance capabilities of Google Cloud. Colab Enterprise is ideal if your project's priorities include collaborative development and reducing the effort to manage infrastructure. Colab Enterprise integrates with Google Cloud services and AI-powered assistance that uses Gemini. Colab Enterprise lets you do the following:

    * Work in notebooks without the need to manage infrastructure.
    * Share a notebook with a single user, Google group, or Google Workspace domain. You can control notebook access through Identity and Access Management (IAM).
    * Interact with features built into Agent Platform and BigQuery.



To track changes and revert to previous versions when necessary, you can integrate your notebooks with version control tools like Git.

### Start with existing and pre-trained models

Training complex models from scratch, especially deep-learning models, requires significant computational resources and time. To accelerate your model selection and development process, start with existing and pre-trained models. These models, which are trained on vast datasets, eliminate the need to train models from scratch and significantly reduce cost and development time.

#### Reduce training and development costs

Select an appropriate model or API for each ML task and combine them to create an end-to-end ML development process.

[Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) offers a vast collection of pre-trained models for tasks such as image classification, object detection, and natural language processing. The models are grouped into the following categories:

  * Google models like the Gemini family of models and Imagen for image generation.
  * Open models like Gemma and Llama.
  * Third-party models from partners like Anthropic.



Google Cloud provides [AI and ML APIs](https://cloud.google.com/ai/apis) that let developers integrate powerful AI capabilities into applications without the need to build models from scratch.

  * [Cloud Vision API](https://docs.cloud.google.com/vision/docs/apis) lets you derive insights from images. This API is valuable for applications like image analysis, content moderation, and automated data entry.
  * [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/apis) lets you analyze text to understand its structure and meaning. This API is useful for tasks like customer feedback analysis, content categorization, and understanding social media trends.
  * [Speech-to-Text API](https://docs.cloud.google.com/speech-to-text/docs/apis) converts audio to text. This API supports a wide range of languages and dialects.
  * [Video Intelligence API](https://docs.cloud.google.com/video-intelligence/docs/apis) analyzes video content to identify objects, scenes, and actions. Use this API for video content analysis, content moderation, and video search.
  * [Document AI API](https://docs.cloud.google.com/document-ai/docs/reference) processes documents to extract, classify, and understand data. This API helps you automate document processing workflows.
  * [Dialogflow API](https://docs.cloud.google.com/dialogflow/cx/docs/reference) enables the creation of conversational interfaces, such as chatbots and voice assistants. You can use this API to create customer service bots and virtual assistants.
  * [Gemini API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference) provides access to Google's most capable and general-purpose AI model.



#### Reduce tuning costs

To help reduce the need for extensive data and compute time, fine-tune your pre-trained models on specific datasets. We recommend the following approaches:

  * **Learning transfer** : Use the knowledge from a pre-trained model for a new task, instead of starting from scratch. This approach requires less data and compute time, which helps to reduce costs.
  * **Adapter tuning ([parameter-efficient tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning#parameter-tuning))**: Adapt models to new tasks or domains without full fine-tuning. This approach requires significantly lower computational resources and a smaller dataset.
  * **[Supervised fine tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning)** : Adapt model behavior with a labeled dataset. This approach simplifies the management of the underlying infrastructure and the development effort that's required for a custom training job.



#### Explore and experiment by using Agent Studio on Gemini Enterprise Agent Platform

[Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio) lets you rapidly test, prototype, and deploy generative AI applications.

  * **Integration with Model Garden** : Provides quick access to the latest models and lets you efficiently deploy the models to save time and costs.
  * **Unified access to specialized models** : Consolidates access to a wide range of pre-trained models and APIs, including those for chat, text, media, translation, and speech. This unified access can help you reduce the time spent searching for and integrating individual services.



### Use managed services to train or serve models

Managed services can help reduce the cost of model training and simplify the infrastructure management, which lets you focus on model development and optimization. This approach can result in significant cost benefits and increased efficiency.

#### Reduce operational overhead

To reduce the complexity and cost of infrastructure management, use managed services such as the following:

  * [Agent Platform Managed Training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview) provides a fully managed environment for training your models at scale. You can choose from various prebuilt containers with popular ML frameworks or use your own custom containers. Google Cloud handles infrastructure provisioning, scaling, and maintenance, so you incur lower operational overhead.
  * [Agent Platform Inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/overview) handles infrastructure scaling, load balancing, and request routing. You get high availability and performance without manual intervention.
  * [Ray on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray) provides a fully managed Ray cluster. You can use the cluster to run complex custom AI workloads that perform many computations (hyperparameter tuning, model fine-tuning, distributed model training, and reinforcement learning from human feedback) without the need to manage your own infrastructure.



#### Use managed services to optimize resource utilization

For details about efficient resource utilization, see [Optimize resource utilization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#optimize_resource_allocation).

## Contributors

Authors: 

  * [Isaac Lo](https://www.linkedin.com/in/isaac-l-25525440) | AI Business Development Manager
  * [Anastasia Prokaeva](https://www.linkedin.com/in/anastasiia-prokaieva) | Field Solutions Architect, Generative AI
  * [Amy Southwood](https://www.linkedin.com/in/amycsouthwood) | Technical Solutions Consultant, Data Analytics, and AI



Other contributors: 

  * [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist



[ Previous arrow_back  Reliability  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability)

[ Next Performance optimization  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-28 UTC."],[],[]] 
