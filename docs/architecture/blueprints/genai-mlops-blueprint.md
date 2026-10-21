---
url: https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint/
title: Build and deploy generative AI and machine learning models in an enterprise \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:33.385238+00:00
---

# Build and deploy generative AI and machine learning models in an enterprise  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Build and deploy generative AI and machine learning models in an enterprise Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-03-28 UTC

As generative AI and machine learning (ML) models become more common in enterprises' business activities and business processes, enterprises increasingly need guidance on model development to ensure consistency, repeatability, security, and safety. To help large enterprises build and deploy generative AI and ML models, we created the _enterprise generative AI and machine learning blueprint_. This blueprint provides you with a comprehensive guide to the entire AI development lifecycle, from preliminary data exploration and experimentation through model training, deployment, and monitoring.

The enterprise generative AI and ML blueprint provides you with many benefits, including the following:

  * **Prescriptive guidance:** Clear guidance on how you can create, configure, and deploy a generative AI and ML development environment that is based on [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform). You can use Vertex AI to develop your own models.
  * **Increased efficiency:** Extensive automation to help reduce the toil from deploying infrastructure and developing generative AI and ML models. Automation lets you focus on value-added tasks such as model design and experimentation.
  * **Enhanced governance and auditability:** Reproducibility, traceability, and controlled deployment of models is incorporated into the design of this blueprint. This benefit lets you better manage your generative AI and ML model lifecycle and helps ensure you can re-train and evaluate models consistently, with clear audit trails.
  * **Security:** The blueprint is designed to be aligned with the requirements of the [National Institute of Standards and Technology (NIST) framework](https://www.nist.gov/cyberframework/framework) and the [Cyber Risk Institute (CRI) framework](https://cyberriskinstitute.org/).



The enterprise generative AI and ML blueprint includes the following:

  * A [GitHub repository](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-genai) that contains a set of Terraform configurations, a [Jupyter notebook](https://jupyter.org/), a [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) definition, a [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs) [directed acyclic graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph), and ancillary scripts. The components in the repository complete the following:

    * The Terraform configuration sets up a Vertex AI model development platform that can support multiple model development teams.
    * The Jupyter notebook lets you develop a model interactively.
    * Managed Airflow DAG provides the primary orchestration framework for your Jupyter notebook in production environments.
    * The Vertex AI Pipelines definition provides an alternative for orchestrating specialized machine learning tasks for container-based workflows and training jobs that are contained entirely within the Vertex AI ecosystem.
    * The ancillary scripts help deploy the Terraform code and pipelines.
  * A guide to the architecture, design, security controls, and operational processes that you use this blueprint to implement (this document).




The enterprise generative AI and ML blueprint is designed to be compatible with the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). The enterprise foundations blueprint provides a number of base-level services that this blueprint relies on, such as [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc). You can deploy the enterprise generative AI and ML blueprint without deploying the enterprise foundations blueprint if your Google Cloud environment provides the necessary functionality to support the enterprise generative AI and ML blueprint.

This document is intended for cloud architects, data scientists, and data engineers who can use the blueprint to build and deploy new generative AI or ML models on Google Cloud. This document assumes that you are familiar with [generative AI and ML model development](https://developers.google.com/learn/topics/datascience) and the [Vertex AI machine learning platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform).

For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

## Enterprise generative AI and ML blueprint overview

The enterprise generative AI and ML blueprint takes a layered approach to provide the capabilities that enable generative AI and ML model training. The blueprint is intended to be deployed and controlled through an [ML operations (MLOps)](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-mlops) workflow. The following diagram shows how the MLOps layer deployed by this blueprint relates to other layers in your environment.

![The blueprint layers.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-layers.svg)

This diagram includes the following:

  * The [Google Cloud infrastructure](https://cloud.google.com/infrastructure) provides you with security capabilities such as [encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit), as well as basic building blocks such as compute and storage.
  * The enterprise foundation provides you with a baseline of resources such as identity, networking, logging, monitoring, and deployment systems that enable you to adopt Google Cloud for your AI workloads.
  * The [data layer](https://docs.cloud.google.com/architecture/data-mesh) is an optional layer in the development stack that provides you with various capabilities such as data ingestion, data storage, data access control, data governance, data monitoring, and data sharing.
  * The generative AI and ML layer (this blueprint) lets you build and deploy models. You can use this layer for preliminary data exploration and experimentation, model training, model serving, and monitoring.
  * CI/CD provides you with the tools to automate the provision, configuration, management, and deployment of infrastructure, workflows, and software components. These components help you ensure consistent, reliable, and auditable deployments; minimize manual errors; and accelerate the overall development cycle.



To show how the generative AI and ML environment is used, the blueprint includes a sample ML model development. The sample model development takes you through building a model, creating operational pipelines, training the model, testing the model, and deploying the model.

## Architecture

The enterprise generative AI and ML blueprint provides you with the ability to work directly with data. You can create models in an interactive (development) environment and promote the models into an operational (production or non-production) environment.

In the interactive environment, you develop ML models using [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction), which is a Jupyter Notebook service that is managed by Google. You build data extraction, data transformation, and model-tuning capabilities in the interactive environment and promote them into the operational environment.

In the operational (non-production) environment, you use pipelines to build and test their models in a repeatable and controllable fashion. After you are satisfied with the performance of the model, you can deploy the model into the operational (production) environment. The following diagram shows the various components of the interactive and operational environments.

![The blueprint architecture.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-architecture.svg)

This diagram includes the following:

  1. **Deployment systems:** Services such as [Service Catalog](https://docs.cloud.google.com/service-catalog) and [Cloud Build](https://docs.cloud.google.com/build) deploy Google Cloud resources into the interactive environment. Cloud Build also deploys Google Cloud resources and model-building workflows into the operational environment.
  2. **Data sources:** Services such as [BigQuery](https://docs.cloud.google.com/bigquery), [Cloud Storage](https://docs.cloud.google.com/storage), [Spanner](https://docs.cloud.google.com/spanner), and [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) host your data. The blueprint provides example data in BigQuery and Cloud Storage.
  3. **Interactive environment:** An environment where you can interact directly with data, experiment on models, and build pipelines for use in the operational environment.
  4. **Operational environment:** An environment where you can build and test your models in a repeatable manner and then deploy models into production.
  5. **Model services:** The following services support various MLOps activities: 
     * [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore#vaifs) serves feature data to your model.
     * [Model Garden](https://docs.cloud.google.com/vertex-ai/docs/start/explore-models) includes an ML model library that lets you use Google models and select open-source models.
     * [Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction) manages the lifecycle of your ML models.
  6. **Artifact storage:** These services store the code and containers and for your model development and pipelines. These services include the following: 
     * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) stores containers that are used by pipelines in the operational environment to control the various stages of the model development.
     * Git repository stores the code base of the various components that are used in the model development.



### Platform personas

When you deploy the blueprint, you create four types of user groups: an MLOps engineer group, a DevOps engineer group, a data scientist group, and a data engineer group. The groups have the following responsibilities:

  * The **MLOps engineer** group develops the Terraform templates used by the Service Catalog. This team provides templates used by many models.
  * The **DevOps engineer** group approves the Terraform templates that the MLOps developer group creates.
  * The **data scientist** group develops models, pipelines, and the containers that are used by the pipelines. Typically, a single team is dedicated to building a single model.
  * The **Data engineer** group approves the use of the artifacts that the data science group creates.



### Organization structure

This blueprint uses the organizational structure of the enterprise foundation blueprint as a basis for deploying AI and ML workloads. The following diagram shows the projects that are added to the foundation to enable AI and ML workloads.

![The blueprint organizational structure.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-org-structure.svg)

The following table describes the projects that are used by the generative AI and ML blueprint.

Folder | Project | Description  
---|---|---  
`common` | `prj-c-infra-pipeline` | Contains the deployment pipeline that's used to build out the generative AI and ML components of the blueprint. For more information, see the [infrastructure pipeline](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology#infrastructure-pipeline) in the enterprise foundation blueprint.   
`prj-c-service-catalog` | Contains the infrastructure used by the Service Catalog to deploy resources in the interactive environment.   
`development` | `prj-d-machine-learning` | Contains the components for developing an AI and ML use case in an interactive mode.  
`non-production` | `prj-n-machine-learning` | Contains the components for testing and evaluating an AI and ML use case that can be deployed to production.  
`production` | `prj-p-machine-learning` | Contains the components for deploying an AI and ML use case into production.   
  
### Networking

The blueprint uses the Shared VPC network created in the enterprise foundation blueprint. In the interactive (development) environment, Vertex AI Workbench notebooks are deployed in service projects. On-premises users can access the projects using the private IP address space in the Shared VPC network. On-premises users can access Google Cloud APIs, such as Cloud Storage, through Private Service Connect. Each Shared VPC network (development, non-production, and production) has a distinct Private Service Connect endpoint.

![The blueprint network.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-networking.svg)

The operational environment (non-production and production) has two separate Shared VPC networks that on-premises resources can access through private IP addresses. The interactive and operational environments are protected using VPC Service Controls.

### Cloud Logging

This blueprint uses the [Cloud Logging](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#centralized-logging) capabilities that are provided by the enterprise foundation blueprint.

### Cloud Monitoring

To [monitor custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics), the blueprint includes a dashboard that lets you monitor the following metrics:

  * CPU utilization of each training node
  * Memory utilization of each training node
  * Network usage



If a custom training job has failed, the blueprint uses Cloud Monitoring to provide you with an email alerting mechanism to notify you of the failure. For monitoring deployed models that use the Vertex AI endpoint, the blueprint comes with a dashboard with that has the following metrics:

  * Performance metrics: 
    * Predictions per second
    * Model latency
  * Resource usage: 
    * CPU usage
    * Memory usage



### Organizational policy setup

In addition to the [organizational policies](https://docs.cloud.google.com/architecture/blueprints/security-foundations/preventative-controls#organization-policy) created by the enterprise foundation blueprint, this blueprint adds the organizational policies listed in [predefined posture for secure AI, extended](https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-secure-ai-template#organization_policy_constraints).

## Operations

This section describes the environments that are included in the blueprint.

### Interactive environment

To let you explore data and develop models while maintaining your organization's security posture, the interactive environment provides you with a controlled set of actions you can perform. You can deploy Google Cloud resources using one of the following methods:

  * Using Service Catalog, which is preconfigured through automation with resource templates
  * Building code artifacts and committing them to Git repositories using Vertex AI Workbench notebooks



The following diagram depicts the interactive environment.

![The blueprint interactive environment.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-interactive-flow.svg)

A typical interactive flow has the following steps and components associated with it:

  1. Service Catalog provides a curated list of Google Cloud resources that data scientists can deploy into the interactive environment. The data scientist deploys the Vertex AI Workbench notebook resource from the Service Catalog.
  2. Vertex AI Workbench notebooks are the main interface that data scientists use to work with Google Cloud resources that are deployed in the interactive environment. The notebooks enable data scientists to pull their code from Git and update their code as needed.
  3. Source data is stored outside of the interactive environment and managed separately from this blueprint. Access to the data is controlled by a [data owner](https://datagovernance.com/assigning-data-ownership/). Data scientists can request read access to source data, but data scientists can't write to the source data.
  4. Data scientists can transfer source data into the interactive environment into resources created through the Service Catalog. In the interactive environment, data scientists can read, write, and manipulate the data. However, data scientists can't transfer data out of the interactive environment or grant access to resources that are created by Service Catalog. BigQuery stores structured data and semi-structured data and Cloud Storage stores unstructured data.
  5. Feature Store provides data scientists with low-latency access to features for model training.
  6. Data scientists train models using Vertex AI [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/create-custom-job). The blueprint also uses Vertex AI for [hyperparameter tuning](https://docs.cloud.google.com/vertex-ai/docs/training/hyperparameter-tuning-overview).

  7. Data scientists evaluate models through the use of [Vertex AI Experiments](https://docs.cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments) and [Vertex AI TensorBoard](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-introduction). Vertex AI Experiments lets you run multiple trainings against a model using different parameters, modeling techniques, architectures, and inputs. Vertex AI TensorBoard lets you track, visualize, and compare the various experiments that you ran and then choose the model with the best observed characteristics to validate.

  8. Data scientists validate their models with [Vertex AI evaluation](https://docs.cloud.google.com/vertex-ai/docs/evaluation/using-model-evaluation). To validate their models, data scientists split the source data into a training data set and a validation data set and run a [Vertex AI evaluation](https://docs.cloud.google.com/vertex-ai/docs/evaluation/using-model-evaluation) against your model.

  9. Data scientists build containers using Cloud Build, store the containers in Artifact Registry, and use the containers in pipelines that are in the operational environment.




### Operational environment

The operational environment uses a Git repository and pipelines. This environment includes the production environment and non-production environment of the enterprise foundation blueprint. In the non-production environment, the data scientist selects a pipeline from one of the pipelines that was developed in the interactive environment. The data scientist can run the pipeline in the non-production environment, evaluate the results, and then determine which model to promote into the production environment.

The blueprint includes an example pipeline that was built using Managed Airflow and an example pipeline that was built using Vertex AI Pipelines. The diagram below shows the operational environment.

![The blueprint operational environment.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-operational-flow.svg)

A typical operational flow has the following steps:

  1. A data scientist merges a development branch successfully into a deployment branch.
  2. The merge into the deployment branch triggers a Cloud Build pipeline.
  3. One of the following items occurs: 
     * If a data scientist is using Managed Airflow as the orchestrator, the Cloud Build pipeline moves a DAG into Cloud Storage.
     * If the data scientist is using Vertex AI Pipelines as the orchestrator, the pipeline moves a Python file into Cloud Storage.
  4. The Cloud Build pipeline triggers the orchestrator (Managed Airflow or Vertex AI Pipelines).
  5. The orchestrator pulls its pipeline definition from Cloud Storage and begins to execute the pipeline.
  6. The pipeline pulls a container from Artifact Registry that is used by all stages of the pipeline to trigger Vertex AI services.
  7. The pipeline, using the container, triggers a data transfer from the source data project into the operational environment.
  8. Data is transformed, validated, split, and prepared for model training and validation by the pipeline.
  9. If needed, the pipeline moves data into Vertex AI Feature Store for easy access during model training.
  10. The pipeline uses Vertex AI custom model training to train the model.
  11. The pipeline uses Vertex AI evaluation to validate the model.
  12. A validated model is [imported](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model) into the [Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction) by the pipeline.
  13. The imported model is then used to generate predictions through [online predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview#online_predictions) or [batch predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview#online_predictions).
  14. After the model is deployed into the production environment, the pipeline uses [Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview) to detect if the model's performance degrades by monitoring for [training-serving skew](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview#calculating-skew-and-drift) and [prediction drift](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview#calculating-skew-and-drift).



## Deployment

The blueprint uses a series of Cloud Build pipelines to provision the blueprint infrastructure, the pipeline in the operational environment, and the containers used to create generative AI and ML models. The pipelines used and the resources provisioned are the following:

  * **[Infrastructure pipeline](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology#infrastructure-pipeline):** This pipeline is part of the enterprise foundation blueprint. This pipeline provisions the Google Cloud resources that are associated with the interactive environment and operational environment.
  * **Interactive pipeline:** The interactive pipeline is part of the interactive environment. This pipeline copies Terraform templates from a Git repository to a Cloud Storage bucket that Service Catalog can read. The interactive pipeline is triggered when a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) is made to merge with the main branch.
  * **Container pipeline:** The blueprint includes a Cloud Build pipeline to build containers used in the operational pipeline. Containers that are deployed across environments are immutable container images. Immutable container images help ensure that the same image is deployed across all environments and cannot be modified while they are running. If you need to modify the application, you must rebuild and redeploy the image. Container images that are used in the blueprint are stored in Artifact Registry and referenced by the configuration files that are used in the operational pipeline.
  * **Operational pipeline:** The operational pipeline is part of the operational environment. This pipeline copies DAGs for Managed Airflow or Vertex AI Pipelines, which are then used to build, test, and deploy models.



### Service Catalog

Service Catalog enables developers and cloud administrators to make their solutions usable by internal enterprise users. The Terraform modules in Service Catalog are built and published as artifacts to the Cloud Storage bucket with the Cloud Build CI/CD pipeline. After the modules are copied to the bucket, developers can use the modules to create Terraform solutions on the Service Catalog Admin page, add the solutions to Service Catalog and share the solutions with interactive environment projects so that users can deploy the resources.

The interactive environment uses Service Catalog to let data scientists deploy Google Cloud resources in a manner that complies with their enterprise's security posture. When developing a model that requires Google Cloud resources, such as a Cloud Storage bucket, the data scientist selects the resource from the Service Catalog, configures the resource, and deploys the resource in the interactive environment. Service Catalog contains pre-configured templates for various Google Cloud resources that the data scientist can deploy in the interactive environment. The data scientist cannot alter the resource templates, but can configure the resources through the configuration variables that the template exposes. The following diagram shows the structure of how the Service Catalog and interactive environment interrelate.

![The blueprint catalog.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-service-catalog.svg)

Data scientists deploy resources using the Service Catalog, as described in the following steps:

  1. The MLOps engineer puts a Terraform resource template for Google Cloud into a Git repository.
  2. The commit to Git triggers a Cloud Build pipeline.
  3. Cloud Build copies the template and any associated configuration files to Cloud Storage.
  4. The MLOps engineer sets up the Service Catalog solutions and Service Catalog manually. The engineer then shares the Service Catalog with a service project in the interactive environment.
  5. The data scientist selects a resource from the Service Catalog.
  6. Service Catalog deploys the template into the interactive environment.
  7. The resource pulls any necessary configuration scripts.
  8. The data scientist interacts with the resources.



### Repositories

The pipelines described in Deployment are triggered by changes in their corresponding repository. To help ensure that no one can make independent changes to the production environment, there is a separation of responsibilities between users who can submit code and users who can approve code changes. The following table describes the blueprint repositories and their submitters and approvers.

Repository | Pipeline | Description | Submitter | Approver  
---|---|---|---|---  
`ml-foundation` | Infrastructure  
| Contains the Terraform code for the generative AI and ML blueprint that creates the interactive and operational environments. | MLOps engineer | DevOps engineer  
`service-catalog` | Interactive | Contains the templates for the resources that the Service Catalog can deploy. | MLOps engineer | DevOps engineer  
`artifact-publish` | Container | Contains the containers that pipelines in the operational environment can use. | Data scientist | Data engineer  
`machine-learning` | Operational | Contains the source code that pipelines in the operational environment can use. | Data scientist | Data engineer  
  
### Branching strategy

The blueprint uses [persistent branching](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology#branching-strategy) to deploy code to the associated environment. The blueprint uses three branches (development, non-production, and production) that reflect the corresponding environments.

## Security controls

The enterprise generative AI and ML blueprint uses a layered defense-in-depth security model that uses default Google Cloud capabilities, Google Cloud services, and security capabilities that are configured through the enterprise foundation blueprint. The following diagram shows the layering of the various security controls for the blueprint.

![The blueprint security controls.](https://docs.cloud.google.com/static/architecture/blueprints/genai-mlops-blueprint/images/mlops-security-controls.svg)

The functions of the layers are the following:

  * **Interface:** provides data scientists with services that allow them to interact with the blueprint in a controlled manner.
  * **Deployment:** provides a series of pipelines that deploy infrastructure, build containers, and create models. The use of pipelines allows for auditability, traceability, and repeatability.
  * **Networking:** provides data exfiltration protections around the blueprint resources at the API layer and the IP layer.
  * **Access management:** controls who can access what resources and helps prevent unauthorized use of your resources.
  * **Encryption:** allows you to control your encryption keys, secrets, and help protect your data through default encryption-at-rest and encryption-in-transit.
  * **Detective:** helps you to detect misconfigurations and malicious activity.
  * **Preventive:** provides you with the means to control and restrict how your infrastructure is deployed.



The following table describes the security controls that are associated with each layer.

Layer | Resource | Security control  
---|---|---  
Interface | Vertex AI Workbench | Provides a managed notebook experience that incorporates [user access control](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/manage-access-jupyterlab), network access control, [IAM access control](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/manage-access), and [disabled file downloads](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create#create). These features enable a more secure user experience.   
Git repositories | Provides user access control to protect your repositories.  
Service Catalog | Provides data scientists with a curated list of resources that can only be deployed in approved configurations.  
Deployment | Infrastructure pipeline | Provides a secured flow to deploy the blueprint infrastructure through the use of Terraform.  
Interactive pipeline | Provides a secured flow to transfer templates from a Git repository into a bucket within your Google Cloud organization.  
Container pipeline | Provides a secured flow to build containers that are used by the operational pipeline.  
Operational pipeline | Provides a controlled flow to train, test, validate, and deploy models.  
Artifact Registry | Stores containers images in a secure manner using resource access control   
Network | Private Service Connect | Lets you communicate with Google Cloud APIs using private IP addresses so that you can avoid exposing traffic to the internet.  
VPC with private IP addresses | The blueprint uses VPCs with private IP addresses to help remove exposure to internet facing threats.  
VPC Service Controls | Helps protect protected resources against data exfiltration.  
Firewall | Helps protect the VPC network against unauthorized access.  
Access management | Cloud Identity | Provides centralized user management, reducing the unauthorized access risk.  
IAM | Provides fine-grained control of who can do what to which resources, thereby enabling least privilege in access management.  
Encryption | Cloud KMS | Lets you control the encryption keys that are used within your Google Cloud organization.  
Secret Manager | Provides a secret store for your models that is controlled by IAM.  
Encryption-at-rest | By default, Google Cloud encrypts data at rest.  
Encryption-in-transit | By default, Google Cloud encrypts data in transit.  
Detective | Security Command Center | Provides threat detectors that help protect your Google Cloud organization.  
Continuous architecture | Continually checks your Google Cloud organization against a series of Open Policy Agent (OPA) policies that you have defined.  
IAM Recommender | Analyzes user permissions and provides suggestions about reducing permissions to help enforce the principle of least privilege.  
Firewall Insights | Analyzes firewall rules, identifies overly-permissive firewall rules, and suggests more restrictive firewalls to help strengthen your overall security posture.   
Cloud Logging | Provides visibility into system activity and helps enable the detection of anomalies and malicious activity.  
Cloud Monitoring | Tracks key signals and events that can help identify suspicious activity.  
Preventative | Organization Policy Service | Lets you restrict actions within your Google Cloud organization.  
  
## What's next

  * Deploy the [Terraform associated with this blueprint](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-genai).
  * Learn more about the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations).
  * Read the [Best practices for implementing machine learning on Google Cloud](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices).
  * Learn more about [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform#ml-workflow).
  * Learn more about MLOps on Google Cloud: 
    * [MLOps on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-mlops)
    * [Practitioners guide to MLOps: A framework for continuous delivery and automation of machine learning](https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf) (PDF)
    * [MLOps: Continuous delivery and automation pipelines in machine learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
    * [Architecture for MLOps using TensorFlow Extended, Vertex AI Pipelines, and Cloud Build](https://docs.cloud.google.com/architecture/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build)
    * [Vertex AI Pipelines sample code](https://github.com/GoogleCloudPlatform/vertex-pipelines-end-to-end-samples)
    * [Vertex AI notebook sample code](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/ml_ops/stage4/get_started_with_vertex_ml_metadata.ipynb)
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-03-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-03-28 UTC."],[],[]] 
