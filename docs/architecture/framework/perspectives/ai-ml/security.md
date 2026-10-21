---
url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security/
title: AI and ML perspective: Security \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:22.990583+00:00
---

# AI and ML perspective: Security  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  AI and ML perspective: Security Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-11-26 UTC

This document in the [Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) provides an overview of principles and recommendations to ensure that your AI and ML deployments meet the security and compliance requirements of your organization. The recommendations in this document align with the [security pillar](https://docs.cloud.google.com/architecture/framework/security) of the Google Cloud Well-Architected Framework.

Secure deployment of AI and ML workloads is a critical requirement, particularly in enterprise environments. To meet this requirement, you need to adopt a holistic security approach that starts from the initial conceptualization of your AI and ML solutions and extends to development, deployment, and ongoing operations. Google Cloud offers robust tools and services that are designed to help secure your AI and ML workloads.

The recommendations in this document are mapped to the following core principles:

  * Define clear goals and requirements
  * Keep data secure and prevent loss or mishandling
  * Keep AI pipelines secure and robust against tampering
  * Deploy on secure systems with secure tools and artifacts
  * Verify and protect inputs
  * Monitor, evaluate, and prepare to respond to outputs



For more information about AI security, you can also review the following resources:

  * [Google Cloud's Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/) provides a comprehensive guide for building secure and responsible AI systems. It outlines key principles and best practices for addressing security and compliance considerations throughout the AI lifecycle.
  * To learn more about Google Cloud's approach to trust in AI, see our [compliance resource center](https://cloud.google.com/compliance).



## Define clear goals and requirements

Effective AI and ML security is a core component of your overarching business strategy. It's easier to integrate the required security and compliance controls early in your design and development process, instead of adding controls after development.

From the start of your design and development process, make decisions that are appropriate for your specific risk environment and your specific business priorities. For example, overly restrictive security measures might protect data but also impede innovation and slow down development cycles. However, a lack of security can lead to data breaches, reputational damage, and financial losses, which are detrimental to business goals.

To define clear goals and requirements, consider the following recommendations.

### Align AI and ML security with business goals

To align your AI and ML security efforts with your business goals, use a strategic approach that integrates security into every stage of the AI lifecycle. To follow this approach, do the following:

  1. **Define clear business objectives and security requirements** :

     * **Identify key business goals** : Define clear business objectives that your AI and ML initiatives are designed to achieve. For example, your objectives might be to improve customer experience, optimize operations, or develop new products.
     * **Translate goals into security requirements** : When you clarify your business goals, define specific security requirements to support those goals. For example, your goal might be to use AI to personalize customer recommendations. To support that goal, your security requirements might be to protect customer data privacy and prevent unauthorized access to recommendation algorithms.
  2. **Balance security with business needs** :

     * **Conduct risk assessments** : Identify potential security threats and vulnerabilities in your AI systems.
     * **Prioritize security measures** : Base the priority of these security measures upon their potential impact on your business goals.
     * **Analyze the costs and benefits** : Ensure that you invest in the most effective solutions. Consider the costs and benefits of different security measures.
     * **Shift left on security** : Implement security best practices early in the design phase, and adapt your safety measures as business needs change and threats emerge.



### Identify potential attack vectors and risks

Consider potential attack vectors that could affect your AI systems, such as data poisoning, model inversion, or adversarial attacks. Continuously monitor and assess the evolving attack surface as your AI system develops, and keep track of new threats and vulnerabilities. Remember that changes in your AI systems can also introduce changes to their attack surface.

To mitigate potential legal and reputational risks, you also need to address compliance requirements related to data privacy, algorithmic bias, and other relevant regulations.

To anticipate potential threats and vulnerabilities early and make design choices that mitigate risks, adopt a _secure by design_ approach.

Google Cloud provides a comprehensive suite of tools and services to help you implement a secure by design approach:

  * **[Cloud posture management](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)** : Use Security Command Center to identify potential vulnerabilities and misconfigurations in your AI infrastructure.
  * **[Attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn)** : Refine and use the attack exposure scores and attack paths that Security Command Center generates.
  * **[Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)** : Stay informed about new threats and attack techniques that emerge to target AI systems.
  * **[Logging and Monitoring](https://docs.cloud.google.com/stackdriver/docs)** : Track the performance and security of your AI systems, and detect any anomalies or suspicious activities. Conduct regular security audits to identify and address potential vulnerabilities in your AI infrastructure and models.
  * **[Vulnerability management](https://cloud.google.com/security/resources/datasheets/consulting-services-threat-and-vulnerability-management)** : Implement a vulnerability management process to track and remediate security vulnerabilities in your AI systems.



For more information, see [Secure by Design at Google](https://research.google/pubs/secure-by-design-at-google/) and [Implement security by design](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design).

## Keep data secure and prevent loss or mishandling

Data is a valuable and sensitive asset that must be kept secure. Data security helps you to maintain user trust, support your business objectives, and meet your compliance requirements.

To help keep your data secure, consider the following recommendations.

### Adhere to data minimization principles

To ensure data privacy, adhere to the principle of data minimization. To minimize data, don't collect, keep, or use data that's not strictly necessary for your business goals. Where possible, use synthetic or fully anonymized data.

Data collection can help drive business insights and analytics, but it's crucial to exercise discretion in the data collection process. If you collect personally identifiable information (PII) about your customer, reveal sensitive information, or create bias or controversy, then you might build biased ML models.

You can use Google Cloud features to help you improve data minimization and data privacy for various use cases:

  * To de-identify your data and also preserve its utility, apply transformation methods like pseudonymization, de-identification, and generalization such as bucketing. To implement these methods, you can use [Sensitive Data Protection](https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp).
  * To enrich data and mitigate potential bias, you can use an [Agent Platform data labeling job](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/label-using-console). The data labeling process adds informative and meaningful tags to raw data, which transforms it into structured training data for ML models. Data labeling adds specificity to the data and reduces ambiguity.
  * To help protect resources from prolonged access or manipulation, use Cloud Storage features to [control data lifecycles](https://docs.cloud.google.com/storage/docs/control-data-lifecycles).



For best practices about how to implement data encryption, see [data encryption at rest and in transit](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design#encrypt_data_at_rest_and_in_transit) in the Well-Architected Framework.

### Monitor data collection, storage, and transformation

Your AI application's training data poses the largest risks for the introduction of bias and data leakage. To stay compliant and manage data across different teams, establish a data governance layer to monitor data flows, transformations, and access. Maintain logs for data access and manipulation activities. The logs help you audit data access, detect unauthorized access attempts, and prevent unwanted access.

You can use Google Cloud features to help you implement data governance strategies:

  * To establish an organization-wide or department-wide data governance platform, use [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs). A data governance platform can help you to centrally discover, manage, monitor, and govern data and AI artifacts across your data platforms. The data governance platform also provides access to trusted users. You can perform the following tasks with Knowledge Catalog: 
    * Manage data lineage. BigQuery can also provide column-level lineage.
    * Manage data quality checks and data profiles.
    * Manage data discovery, exploration, and processing across different data marts.
    * Manage feature metadata and model artifacts.
    * Create a business glossary to manage metadata and establish a standardized vocabulary.
    * [Enrich the metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata) with context through aspects and aspect types.
    * Unify data governance across BigLake and open-format tables like Iceberg and Delta.
    * Build a [data mesh](https://docs.cloud.google.com/architecture/data-mesh) to decentralize data ownership among data owners from different teams or domains. This practice adheres to data security principles and it can help improve data accessibility and operational efficiency.
    * [Inspect and send sensitive data results](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job) from BigQuery to Knowledge Catalog.
  * To build a unified open [lakehouse](https://cloud.google.com/discover/what-is-a-data-lakehouse) that is well-governed, integrate your data lakes and warehouses with managed metastore services like [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/overview) and [Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-blms). An open lakehouse uses open table formats that are compatible with different data processing engines.
  * To schedule the monitoring of features and feature groups, use [Agent Platform Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/monitor-features#create-feature-monitor).
  * To scan your Agent Platform datasets at the organization, folder, or project level, use [Sensitive data discovery for Agent Platform](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). You can also [analyze the data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles) that are stored in BigQuery.
  * To capture real-time logs and collect metrics related to data pipelines, use [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) and [Cloud Monitoring](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs). To collect audit trails of API calls, use [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). Don't log PII or confidential data in experiments or in different log servers.



### Implement role-based access controls with least privilege principles

Implement role-based access controls (RBAC) to assign different levels of access based on user roles. Users must have only the minimum permissions that are necessary to let them perform their role activities. Assign permissions based on the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) so that users have only the access that they need, such as no-access, read-only, or write.

RBAC with least privilege is important for security when your organization uses sensitive data that resides in data lakes, in feature stores, or in hyperparameters for model training. This practice helps you to prevent data theft, preserve model integrity, and limit the surface area for accidents or attacks.

To help you implement these access strategies, you can use the following Google Cloud features:

  * To implement access granularity, consider the following options:

    * Map the IAM roles of different products to a user, group, or service account to allow granular access. Map these roles based on your project needs, access patterns, or [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).
    * Set [IAM policies with conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to manage granular access to your data, model, and model configurations, such as code, resource settings, and hyperparameters.
    * Explore application-level granular access that helps you secure sensitive data that you audit and share outside of your team.

      * **Cloud Storage** : Set IAM policies on [buckets and managed folders](https://docs.cloud.google.com/storage/docs/access-control/iam).
      * **BigQuery** : Use [IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control) for datasets and resources within datasets. Also, restrict access at the [row-level](https://docs.cloud.google.com/bigquery/docs/managing-row-level-security) and [column-level](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) in BigQuery.
  * To limit access to certain resources, you can use [principal access boundary (PAB) policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-create). You can also use [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/temporary-elevated-access) to control just-in-time, temporary privilege elevation for select principals. Later, you can view the audit logs for this Privileged Access Manager activity.

  * To restrict access to resources based on the IP address and end user device attributes, you can [extend Identity-Aware Proxy (IAP) access policies](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto).

  * To create access patterns for different user groups, you can use [Agent Platform access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control) to combine the predefined or custom roles.

  * To protect Gemini Enterprise Agent Platform Workbench instances by using context-aware access controls, use [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs) and [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels). With this approach, access is evaluated each time a user authenticates to the instance.




### Implement security measures for data movement

Implement secure perimeters and other measures like encryption and restrictions on data movement. These measures help you to prevent data exfiltration and data loss, which can cause financial losses, reputational damage, legal liabilities, and a disruption to business operations.

To help prevent data exfiltration and loss on Google Cloud, you can use a combination of security tools and services.

To implement encryption, consider the following:

  * To gain more control over encryption keys, use customer-managed encryption keys (CMEKs) in Cloud KMS. When you use CMEKs, the following CMEK-integrated services encrypt data at rest for you: 
    * [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/cmek)
    * [Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys)
    * [Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/cmek)
    * [Spanner](https://docs.cloud.google.com/spanner/docs/cmek)
    * [BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption)
  * To help protect your data in Cloud Storage, use server-side encryption to store your CMEKs. If you manage CMEKs on your own servers, server-side encryption can help protect your CMEKs and associated data, even if your CMEK storage system is compromised.
  * To encrypt data in transit, use HTTPS for all of your API calls to AI and ML services. To enforce HTTPS for your applications and APIs, use [HTTPS load balancers](https://docs.cloud.google.com/load-balancing/docs/https).



For more best practices about how to encrypt data, see [Encrypt data at rest and in transit](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design#encrypt_data_at_rest_and_in_transit) in the security pillar of the Well-Architected Framework.

To implement perimeters, consider the following:

  * To create a security boundary around your AI and ML resources and prevent data exfiltration from your Virtual Private Cloud (VPC), use [VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls) to define a service perimeter. Include your AI and ML resources and sensitive data in the perimeter. To control data flow, configure ingress and egress rules for your perimeter.
  * To restrict inbound and outbound traffic to your AI and ML resources, [configure firewall rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview). Implement policies that deny all traffic by default and explicitly allow only the traffic that meets your criteria. For a policy example, see [Example: Deny all external connections except to specific ports](https://docs.cloud.google.com/firewall/docs/network-firewall-policy-examples#deny-all-external-connections-except-to-specific-ports).



To implement restrictions on data movement, consider the following:

  * To share data and to scale across privacy boundaries in a secure environment, use [BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction) and [BigQuery data clean rooms](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms), which provide a robust security and privacy framework.
  * To share data directly into built-in destinations from business intelligence dashboards, use [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub), which provides a secure cloud environment.



### Guard against data poisoning

_Data poisoning_ is a type of cyberattack in which attackers inject malicious data into training datasets to manipulate model behavior or to degrade performance. This cyberattack can be a serious threat to ML training systems. To protect the validity and quality of the data, maintain practices that guard your data. This approach is crucial for consistent unbiasedness, reliability, and integrity of your model.

To track inconsistent behavior, transformation, or unexpected access to your data, set up comprehensive monitoring and alerting for data pipelines and ML pipelines.

Google Cloud features can help you implement more protections against data poisoning:

  * To validate data integrity, consider the following:

    * Implement robust data validation checks before you use the data for training. Verify data formats, ranges, and distributions. You can use the automatic data quality capabilities in [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview).
    * Use Sensitive Data Protection with Model Armor to take advantage of comprehensive data loss prevention capabilities. For more information, see [Model Armor key concepts](https://docs.cloud.google.com/security-command-center/docs/key-concepts-model-armor). Sensitive Data Protection with Model Armor lets you discover, classify, and protect sensitive data such as intellectual property. These capabilities can help you prevent the unauthorized exposure of sensitive data in LLM interactions.
    * To detect anomalies in your training data that might indicate data poisoning, use [anomaly detection in BigQuery](https://docs.cloud.google.com/bigquery/docs/anomaly-detection-overview) with statistical methods or ML models.
  * To prepare for robust training, do the following:

    * Employ [ensemble methods](https://en.wikipedia.org/wiki/Ensemble_learning) to reduce the impact of poisoned data points. Train multiple models on different subsets of the data with [hyperparameter tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuning-overview).
    * Use data augmentation techniques to balance the distribution of data across datasets. This approach can reduce the impact of data poisoning and lets you add adversarial examples.
  * To incorporate human review for training data or model outputs, do the following:

    * Analyze model evaluation metrics to detect potential biases, anomalies, or unexpected behavior that might indicate data poisoning. For details, see [Model evaluation in Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction).
    * Take advantage of domain expertise to evaluate the model or application and identify suspicious patterns or data points that automated methods might not detect. For details, see [Gen AI evaluation service overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview).



For best practices about how to create data platforms that focus on infrastructure and data security, see the [Implement security by design](https://docs.cloud.google.com/architecture/framework/security/data-security) principle in the Well-Architected Framework.

## Keep AI pipelines secure and robust against tampering

Your AI and ML code and the code-defined pipelines are critical assets. Code that isn't secured can be tampered with, which can lead to data leaks, compliance failure, and disruption of critical business activities. Keeping your AI and ML code secure helps to ensure the integrity and value of your models and model outputs.

To keep AI code and pipelines secure, consider the following recommendations.

### Use secure coding practices

To prevent vulnerabilities, use secure coding practices when you develop your models. We recommend that you implement AI-specific input and output validation, manage all of your software dependencies, and consistently embed secure coding principles into your development. Embed security into every stage of the AI lifecycle, from data preprocessing to your final application code.

To implement rigorous validation, consider the following:

  * To prevent model manipulation or system exploits, validate and sanitize inputs and outputs in your code.

    * Use Model Armor or fine-tuned LLMs to automatically screen prompts and responses for common risks.
    * Implement data validation within your data ingestion and preprocessing scripts for data types, formats, and ranges. For [Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) or BigQuery, you can use Python to implement this data validation.
    * Use coding assistant LLM agents, like [CodeMender](https://cloud.google.com/security/codemender), to improve code security. Keep a human in the loop to validate its proposed changes.
  * To manage and secure your AI model API endpoints, use [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee), which includes configurable features like request validation, traffic control, and authentication.

  * To help mitigate risk throughout the AI lifecycle, you can use [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) to do the following:

    * Discover AI inventory in your environment.
    * Assess the inventory for potential vulnerabilities.
    * Secure AI assets with controls, policies, and protections.
    * Manage AI systems with detection, investigation, and response capabilities.



To help secure the code and artifact dependencies in your CI/CD pipeline, consider the following:

  * To address the risks that open-source library dependencies can introduce to your project, use [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) with [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to detect known vulnerabilities. Use and maintain the approved versions of libraries. Store your custom ML packages and vetted dependencies in a private Artifact Registry repository.
  * To embed dependency scanning into your Cloud Build MLOps pipelines, use [Binary Authorization](https://docs.cloud.google.com/build/docs/securing-builds/secure-deployments-to-run-gke). Enforce policies that allow deployments only if your code's container images pass the security checks.
  * To get security information about your software supply chain, use [dashboards](https://docs.cloud.google.com/monitoring/dashboards) in the Google Cloud console that provide details about sources, builds, artifacts, deployments, and runtimes. This information includes vulnerabilities in build artifacts, build provenance, and Software Bill of Materials (SBOM) dependency lists.
  * To assess the maturity level of your software supply chain security, use the [Supply chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/spec/v1.0/levels).



To consistently embed secure coding principles into every stage of development, consider the following:

  * To prevent the exposure of sensitive data from model interactions, use Logging with Sensitive Data Protection. When you use these products together, you can control what data your AI applications and pipeline components log, and hide sensitive data.
  * To implement the principle of least privilege, ensure that the service accounts that you use for your Agent Platform custom jobs, pipelines, and deployed models have only the minimum required IAM permissions. For more information, see Implement role-based access controls with least privilege principles.
  * To help secure and protect your pipelines and build artifacts, understand the security configurations (VPC and VPC Service Controls) in the environment your code runs in.



### Protect pipelines and model artifacts from unauthorized access

Your model artifacts and pipelines are intellectual property, and their training data also contains proprietary information. To protect model weights, files, and deployment configurations from tampering and vulnerabilities, store and access these artifacts with improved security. Implement different access levels for each artifact based on user roles and needs.

To help secure your model artifacts, consider the following:

  * To protect model artifacts and other sensitive files, encrypt them with Cloud KMS. This encryption helps to protect data at rest and in transit, even if the underlying storage becomes compromised.
  * To help secure access to your files, store them in Cloud Storage and configure access controls.
  * To track any incorrect or inadequate configurations and any drift from your defined standards, use Security Command Center to configure [security postures](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview).
  * To enable fine-grained access control and encryption at rest, store your model artifacts in [Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). For additional security, create a digital signature for packages and containers that are produced during the approved build processes.
  * To benefit from Google Cloud's enterprise-grade security, use models that are available in Model Garden. Model Garden provides Google's proprietary models and it offers [third-party models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models#model_security_scanning) from featured partners.
  * To enforce central management for all user and group lifecycles and to enforce the principle of least privilege, use IAM.

    * Create and use dedicated, least-privilege service accounts for your MLOps pipelines. For example, a training pipeline's service account has the permissions to read data from only a specific Cloud Storage bucket and to write model artifacts to Model Registry.
    * Use IAM Conditions to enforce conditional, attribute-based access control. For example, a condition allows a service account to trigger a Agent Platform pipeline only if the request originates from a trusted Cloud Build trigger.



To help secure your deployment pipelines, consider the following:

  * To manage MLOps stages on Google Cloud services and resources, use Agent Platform Pipelines, which can integrate with other services and provide low-level access control. When you re-execute the pipelines, ensure that you perform explainability evaluations (such as feature attributions) and [responsible AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai) checks before you deploy the model artifacts. These checks can help you detect or prevent the following security issues:

    * Unauthorized changes, which can indicate model tampering.
    * Cross-site scripting (XSS), which can indicate compromised container images or dependencies.
    * Insecure endpoints, which can indicate misconfigured serving infrastructure.
  * To help secure model interactions during inference, use private endpoints based on [Private Service Connect](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/private-service-connect) with [prebuilt containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/pre-built-containers) or [custom containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-custom-container). Create model signatures with a predefined input and output schema.

  * To automate code change tracking, use Git for source code management, and integrate version control with robust CI/CD pipelines.




For more information, see [Secure AI Framework (SAIF)](https://cloud.google.com/use-cases/secure-ai-framework).

### Enforce lineage and tracking

To help meet the regulatory compliance requirements that you might have, enforce lineage and tracking of your AI and ML assets. Data lineage and tracking provides extensive change records for data, models, and code. Model provenance provides transparency and accountability throughout the AI and ML lifecycle.

To effectively enforce lineage and tracking in Google Cloud, consider the following tools and services:

  * To track the lineage of models, datasets, and artifacts that are automatically encrypted at rest, use [Agent Platform ML Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/introduction#ml_artifact_lineage). Log metadata about data sources, transformations, model parameters, and experiment results.
  * To track the [lineage of pipeline artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage) from Agent Platform Pipelines, and to search for model and dataset resources, you can use Knowledge Catalog. Track individual pipeline artifacts when you want to perform debugging, troubleshooting, or a root cause analysis. To track your entire MLOps pipeline, which includes the lineage of pipeline artifacts, use [Agent Platform ML Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/analyzing). Agent Platform ML Metadata also lets you analyze the resources and runs. Model Registry applies and manages the versions of each model that you store.
  * To track API calls and administrative actions, enable [audit logs for Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/audit-logging). [Analyze audit logs](https://docs.cloud.google.com/logging/docs/analyze/query-and-view) with Observability Analytics to understand who accessed or modified data and models, and when. You can also [route logs to third-party destinations](https://docs.cloud.google.com/logging/docs/export/pubsub#integrate-thru-pubsub).



## Deploy on secure systems with secure tools and artifacts

Ensure that your code and models run in a secure environment. This environment must have a robust access control system and provide security assurances for the tools and artifacts that you deploy.

To deploy your code on secure systems, consider the following recommendations.

### Train and deploy models in a secure environment

To maintain system integrity, confidentiality, and availability for your AI and ML systems, implement stringent access controls that prevent unauthorized resource manipulation. This defense helps you to do the following:

  * Mitigate model tampering that could produce unexpected or conflicting results.
  * Protect your training data from privacy violations.
  * Maintain service uptime.
  * Maintain regulatory compliance.
  * Build user trust.



To train your ML models in an environment with improved security, use managed services in Google Cloud like Cloud Run, GKE, and Managed Service for Apache Spark. You can also use [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview).

This section provides recommendations to help you further help secure your training and deployment environment.

To help secure your environment and perimeters, consider the following:

  * When you implement security measures, as described earlier, consider the following:

    * To isolate training environments and limit access, use [dedicated projects or VPCs](https://docs.cloud.google.com/architecture/best-practices-vpc-design) for training.
    * To protect sensitive data and code during execution, use [Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) or [confidential computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) for training workloads.
    * To help secure your network infrastructure and to control access to your deployed models, use VPCs, firewalls, and security perimeters.
  * When you use Gemini Enterprise Agent Platform Managed Training, you can use the following methods to help secure your compute infrastructure:

    * To train custom jobs that privately communicate with other authorized Google Cloud services and that aren't exposed to public traffic, [set up a Private Service Connect interface](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-psc-i-setup).
    * For increased network security and lower network latency than what you get with a public IP address, use a private IP address to connect to your training jobs. For details, see [Use a private IP for custom training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/using-private-ip).
  * When you use GKE or Cloud Run to set up a custom environment, consider the following options:

    * To secure your GKE cluster, use the appropriate network policies, pod security policies, and access controls. Use [trusted and verified container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#containerd) for your training workloads. To [scan container images](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically) for vulnerabilities, use Artifact Analysis.
    * To protect your environment from [container escapes](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-engine-container-escape) and other attacks, implement [runtime security measures](https://docs.cloud.google.com/functions/docs/securing/execution-environment-security) for Cloud Run functions. To further protect your environment, use [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) and [workload isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation).
    * To help secure your GKE workloads, follow the best practices in the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
    * To help meet your security requirements in Cloud Run, see the [security design overview}](https://docs.cloud.google.com/run/docs/securing/security).
  * When you use Managed Service for Apache Spark for model training, follow the [Managed Service for Apache Spark security best practices](https://docs.cloud.google.com/dataproc/docs/concepts/security-best-practices).




To help secure your deployment, consider the following:

  * When you deploy models, use Model Registry. If you deploy models in containers, use GKE Sandbox and [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) to enhance security and isolate workloads. [Restrict access to models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access) from Model Garden according to user roles and responsibilities.
  * To help secure your model APIs, use Apigee or [API Gateway](https://docs.cloud.google.com/api-gateway/docs). To prevent abuse, implement API keys, authentication, authorization, and rate limiting. To control access to model APIs, use API keys and authentication mechanisms.
  * To help secure access to models during prediction, use [Gemini Enterprise Agent Platform Inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/overview). To prevent data exfiltration, use VPC Service Controls perimeters to protect [private endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/using-private-endpoints) and govern access to the underlying models. You use private endpoints to enable access to the models within a VPC network. [IAM isn't directly applied](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/endpoint-access-control) to the private endpoint, but the target service uses IAM to manage access to the models. For online prediction, we recommend that you use Private Service Connect.
  * To track API calls that are related to model deployment, enable [Cloud Audit Logs for Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/audit-logging). Relevant API calls include activities such as endpoint creation, model deployment, and configuration updates.
  * To extend Google Cloud infrastructure to edge locations, consider [Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/docs/overview) solutions. For a fully disconnected solution, you can use [Distributed Cloud air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/overview), which doesn't require connectivity to Google Cloud.
  * To help standardize deployments and to help ensure compliance with regulatory and security needs, use [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).



### Follow SLSA guidelines for AI artifacts

Follow the standard [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) guidelines for your AI-specific artifacts, like models and software packages.

SLSA is a security framework that's designed to help you improve the integrity of software artifacts and help prevent tampering. When you adhere to the SLSA guidelines, you can enhance the security of your AI and ML pipeline and the artifacts that the pipeline produces. SLSA adherence can provide the following benefits:

  * **Increased trust in your AI and ML artifacts** : SLSA helps to ensure that tampering doesn't occur to your models and software packages. Users can also trace models and software packages back to their source, which increases users' confidence in the integrity and reliability of the artifacts.
  * **Reduced risk of supply chain attacks** : SLSA helps to mitigate the risk of attacks that exploit vulnerabilities in the software supply chain, like attacks that inject malicious code or that compromise build processes.
  * **Enhanced security posture** : SLSA helps you to strengthen the overall security posture of your AI and ML systems. This implementation can help reduce the risk of attacks and protect your valuable assets.



To implement SLSA for your AI and ML artifacts on Google Cloud, do the following:

  1. **Understand SLSA levels** : Familiarize yourself with the different [SLSA levels](https://slsa.dev/spec/v1.0/levels) and their requirements. As the levels increase, the integrity that they provide also increases.
  2. **Assess your current level** : Evaluate your current practices against the SLSA framework to determine your current level and to identify areas for improvement.
  3. **Set your target level** : Determine the appropriate SLSA level to target based on your risk tolerance, security requirements, and the criticality of your AI and ML systems.
  4. **Implement SLSA requirements** : To meet your target SLSA level, [implement the necessary controls and practices](https://docs.cloud.google.com/software-supply-chain-security/docs/overview), which could include the following:

     * **Source control** : Use a version control system like Git to track changes to your code and configurations.
     * **Build process** : Use a service that helps to secure your builds, like [Cloud Build](https://docs.cloud.google.com/build), and ensure that your build process is scripted or automated.
     * **Provenance generation** : Generate provenance metadata that captures details about how your artifacts were built, including the build process, source code, and dependencies. For details, see [Track metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/tracking) and [Track executions and artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/track-executions-artifacts).
     * **Artifact signing** : Sign your artifacts to verify their authenticity and integrity.
     * **Vulnerability management** : Scan your artifacts and dependencies for vulnerabilities on a regular basis. Use tools like [Artifact Analysis.](https://docs.cloud.google.com/artifact-registry/docs/analysis)
     * **Deployment security** : Implement deployment practices that help to secure your systems, such as the practices that are described in this document.
  5. **Continuous improvement** : Monitor and improve your SLSA implementation to address new threats and vulnerabilities, and strive for higher SLSA levels.




### Use validated prebuilt container images

To prevent a single point of failure for your MLOps stages, isolate the tasks that require different dependency management into different containers. For example, use separate containers for feature engineering, training or fine-tuning, and inference tasks. This approach also gives ML engineers the flexibility to control and customize their environment.

To promote MLOps consistency across your organization, use prebuilt containers. Maintain a central repository of verified and trusted base platform images with the following best practices:

  * Maintain a centralized platform team in your organization that builds and manages standardized base containers.
  * Extend the prebuilt container images that Agent Platform provides specifically for AI and ML. Manage the container images in a central repository within your organization.



Agent Platform provides a variety of [prebuilt containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/pre-built-containers) for training and inference, and it also lets you use [custom containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/containers-overview). For smaller models, you can reduce latency for inference if you [load models in containers](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#model-container).

To improve the security of your container management, consider the following recommendations:

  * Use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to create, store, and manage repositories of container images with different formats. Artifact Registry handles access control with IAM, and it has integrated observability and [vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment) features. Artifact Registry lets you enable container security features, scan container images, and investigate vulnerabilities.
  * Run [continuous integration](https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke) steps and [build container images](https://docs.cloud.google.com/build/docs/building/build-containers) with Cloud Build. Dependency issues can be highlighted at this stage. If you want to deploy only the images that are built by Cloud Build, you can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/cloud-build). To help prevent supply chain attacks, deploy the images built by Cloud Build in Artifact Registry. Integrate automated testing tools such as SonarQube, PyLint, or OWASP ZAP.
  * Use a container platform like GKE or Cloud Run, which are optimized for GPU or TPU for AI and ML workloads. Consider the [vulnerability scanning options](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) for containers in GKE clusters.



### Consider Confidential Computing for GPUs

To protect [_data in use_](https://en.wikipedia.org/wiki/Digital_data#Data_in_use), you can use Confidential Computing. Conventional security measures protect data at rest and in transit, but Confidential Computing encrypts data during processing. When you use Confidential Computing for GPUs, you help to protect sensitive training data and model parameters from unauthorized access. You can also help to prevent unauthorized access from privileged cloud users or potential attackers who might gain access to the underlying infrastructure.

To determine whether you need Confidential Computing for GPUs, consider the sensitivity of the data, regulatory requirements, and potential risks.

If you set up Confidential Computing, consider the following options:

  * For general-purpose AI and ML workloads, use [Confidential VM instances](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with NVIDIA T4 GPUs. These VM instances offer hardware-based encryption of data in use.
  * For containerized workloads, use [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes). These nodes provide a secure and isolated environment for your pods.
  * To ensure that your workload is running in a genuine and secure enclave, [verify the attestation](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation) reports that Confidential VM provides.
  * To track performance, resource utilization, and security events, monitor your Confidential Computing resources and your Confidential GKE Nodes by using Monitoring and Logging.



## Verify and protect inputs

Treat all of the inputs to your AI systems as untrusted, regardless of whether the inputs are from end users or other automated systems. To help keep your AI systems secure and to ensure that they operate as intended, you must detect and sanitize potential attack vectors early.

To verify and protect your inputs, consider the following recommendations.

### Implement practices that help secure generative AI systems

Treat prompts as a critical application component that has the same importance to security as code does. Implement a [defense-in-depth](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\)) strategy that combines proactive design, automated screening, and disciplined lifecycle management.

To help secure your generative AI prompts, you must design them for security, screen them before use, and manage them throughout their lifecycle.

To improve the security of your prompt design and engineering, consider the following practices:

  * **Structure prompts for clarity** : Design and test all of your prompts by using [Agent Studio on Gemini Enterprise Agent Platform prompt management capabilities](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/prompt-classes). Prompts need to have a clear, unambiguous structure. Define a role, [include few-shot examples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/few-shot-examples), and give specific, bounded instructions. These methods reduce the risk that the model might misinterpret a user's input in a way that creates a security loophole.
  * **Test the inputs for robustness and grounding** : Test all of your systems proactively against unexpected, malformed, and malicious inputs in order to prevent crashes or insecure outputs. Use red team testing to simulate real-world attacks. As a standard step in your Agent Platform Pipelines, automate your robustness tests. You can use the following testing techniques:

    * Fuzz testing.
    * Test directly against PII, sensitive inputs, and SQL injections.
    * Scan multimodal inputs that can contain malware or violate prompt policies.
  * **Implement a layered defense** : Use multiple defenses and never rely on a single defensive measure. For example, for an application based on retrieval-augmented generation (RAG), use a separate LLM to classify incoming user intent and check for malicious patterns. Then, that LLM can pass the request to the more-powerful primary LLM that generates the final response.

  * **Sanitize and validate inputs** : Before you incorporate external input or user-provided input into a prompt, filter and validate all of the input in your application code. This validation is important to help you prevent indirect prompt injection.




For automated prompt and response screening, consider the following practices:

  * **Use comprehensive security services** : Implement a dedicated, model-agnostic security service like Model Armor as a mandatory protection layer for your LLMs. Model Armor inspects prompts and responses for threats like prompt injection, [jailbreak attempts](https://en.wikipedia.org/wiki/Privilege_escalation#Jailbreaking), and harmful content. To help ensure that your models don't leak sensitive training data or intellectual property in their responses, use the Sensitive Data Protection integration with Model Armor. For details, see [Model Armor filters](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview#ma-filters).
  * **Monitor and log interactions** : Maintain detailed logs for all of the prompts and responses for your model endpoints. Use [Logging](https://docs.cloud.google.com/logging) to audit these interactions, identify patterns of misuse, and detect attack vectors that might emerge against your deployed models.



To help secure prompt lifecycle management, consider the following practices:

  * **Implement versioning for prompts** : Treat all of your production prompts like application code. Use a version control system like Git to create a complete history of changes, enforce collaboration standards, and enable rollbacks to previous versions. This core MLOps practice can help you to maintain stable and secure AI systems.
  * **Centralize prompt management** : Use a central repository to store, manage, and deploy all of your versioned prompts. This strategy enforces consistency across environments and it enables runtime updates without the need for a full application redeployment.
  * **Conduct regular audits and red team testing** : Test your system's defenses continuously against known vulnerabilities, such as those listed in the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). As an AI engineer, you must be proactive and red-team test your own application to discover and remediate weaknesses before an attacker can exploit them.



### Prevent malicious queries to your AI systems

Along with authentication and authorization, which this document discussed earlier, you can take further measures to help secure your AI systems against malicious inputs. You need to prepare your AI systems for _post-authentication_ scenarios in which attackers bypass both the authentication and authorization protocols, and then attempt to attack the system internally.

To implement a comprehensive strategy that can help protect your system from post-authentication attacks, apply the following requirements:

  * **Secure network and application layers** : Establish a multi-layered defense for all of your AI assets.

    * To create a security perimeter that prevents data exfiltration of models from Model Registry or of sensitive data from BigQuery, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Always use [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) to validate the impact of a perimeter before you enforce it.
    * To help protect web-based tools such as notebooks, use [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview).
    * To help secure all of the inference endpoints, use [Apigee](https://docs.cloud.google.com/apigee) for enterprise-grade security and governance. You can also use API Gateway for straightforward authentication.
  * **Watch for query pattern anomalies** : For example, an attacker that probes a system for vulnerabilities might send thousands of slightly different, sequential queries. Flag abnormal query patterns that don't reflect normal user behavior.

  * **Monitor the volume of requests** : A sudden spike in query volume strongly indicates a denial-of-service (DoS) attack or a model theft attack, which is an attempt to reverse-engineer the model. Use rate limiting and throttling to control the volume of requests from a single IP address or user.

  * **Monitor and set alerts for geographic and temporal anomalies** : Establish a baseline for normal access patterns. Generate alerts for sudden activity from unusual geographic locations or at odd hours. For example, a massive spike in logins from a new country at 3 AM.




## Monitor, evaluate, and prepare to respond to outputs

AI systems deliver value because they produce outputs that augment, optimize, or automate human decision-making. To maintain the integrity and trustworthiness of your AI systems and applications, ensure that the outputs are secure and within the expected parameters. You also need a plan to respond to incidents.

To maintain your outputs, consider the following recommendations.

### Evaluate model performance with metrics and security measures

To ensure that your AI models meet performance benchmarks, meet security requirements, and adhere to fairness and compliance standards, thoroughly evaluate the models. Conduct evaluations before deployment, and then continue to evaluate the models in production on a regular basis. To minimize risks and build trustworthy AI systems, implement a comprehensive evaluation strategy that combines performance metrics with specific AI security assessments.

To evaluate model robustness and security posture, consider the following recommendations:

  * Implement model signing and verification in your MLOps pipeline.

    * For containerized models, use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/cloud-build) to verify signatures.
    * For models that are deployed directly to Agent Platform endpoints, use custom checks in your deployment scripts for verification.
    * For any model, use Cloud Build for model signing.
  * Assess your model's resilience to unexpected or adversarial inputs.

    * For all of your models, test your model for common data corruptions and any potentially malicious data modifications. To orchestrate these tests, you can use Gemini Enterprise Agent Platform Managed Training or Agent Platform Pipelines.
    * For security-critical models, conduct adversarial attack simulations to understand the potential vulnerabilities.
    * For models that are deployed in containers, use Artifact Analysis in Artifact Registry to scan the base images for vulnerabilities.
  * Use Model Monitoring on Gemini Enterprise Agent Platform to detect drift and skew for deployed models. Then, feed these insights back into the re-evaluation or retraining cycles.

  * Use model evaluations from Agent Platform as a pipeline component with Agent Platform Pipelines. You can run the model evaluation component by itself or with other pipeline components. Compare the model versions against your defined metrics and datasets. Log the evaluation results to Agent Platform ML Metadata for lineage and tracking.

  * Use or build upon the [Gen AI evaluation service](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview) to evaluate your chosen models or to implement custom human-evaluation workflows.




To assess fairness, bias, explainability, and factuality, consider the following recommendations:

  * [Define fairness measures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/intro-evaluation-fairness) that match your use cases, and then evaluate your models for potential biases across different data slices.
  * Understand which features drive model predictions in order to ensure that the features, and the predictions that result, align with domain knowledge and ethical guidelines.
  * Use explainability techniques to get feature attributions for your models.
  * Use the Gen AI evaluation service to compute metrics. During the source verification phase of testing, the service's grounding metric checks for factuality against the source text that's provided.
  * Enable [grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview) for your model's output in order to facilitate a second layer of source verification at the user level.
  * Review our [AI principles](https://ai.google/principles/) and adapt them for your AI applications.



### Monitor AI and ML model outputs in production

Continuously monitor your AI and ML models and their supporting infrastructure in production. It's important to promptly identify and diagnose degradations in model output quality or performance, security vulnerabilities that emerge, and deviations from compliance mandates. This monitoring helps you sustain system safety, reliability, and trustworthiness.

To monitor AI system outputs for anomalies, threats, and quality degradation, consider the following recommendations:

  * Use Model Monitoring on Agent Platform for your model outputs to track unexpected shifts in prediction distributions or spikes in low-confidence model predictions. Actively monitor your generative AI model outputs for generated content that's unsafe, biased, off-topic, or malicious. You can also use Model Armor to screen all of your model outputs.
  * Identify specific error patterns, capture quality indicators, or detect harmful or non-compliant outputs at the application level. To find these issues, use custom monitoring in Monitoring dashboards and use log-based metrics from Logging.



To monitor outputs for security-specific signals and unauthorized changes, consider the following recommendations:

  * Identify unauthorized access attempts to AI models, datasets in Cloud Storage or BigQuery, or MLOps pipeline components. In particular, identify unexpected or unauthorized changes in IAM permissions for AI resources. To track these activities and review them for suspicious patterns, use the Admin Activity audit logs and Data Access audit logs in Cloud Audit Logs. Integrate the findings from Security Command Center, which can flag security misconfigurations and flag potential threats that are relevant to your AI assets.
  * Monitor outputs for high volumes of requests or requests from suspicious sources, which might indicate attempts to reverse engineer models or exfiltrate data. You can also use Sensitive Data Protection to monitor for the exfiltration of potentially sensitive data.
  * Integrate logs into your security operations. Use Google Security Operations to help you detect, orchestrate, and respond to any cyber threats from your AI systems.



To track the operational health and performance of the infrastructure that serves your AI models, consider the following recommendations:

  * Identify operational issues that can impact service delivery or model performance.
  * Monitor Agent Platform endpoints for latency, error rates, and traffic patterns.
  * Monitor MLOps pipelines for execution status and errors.
  * Use Monitoring, which provides ready-made metrics. You can also create custom dashboards to help you identify issues like endpoint outages or pipeline failures.



### Implement alerting and incident response procedures

When you identify any potential performance, security, or compliance issues, an effective response is critical. To ensure timely notifications to the appropriate teams, implement robust alerting mechanisms. Establish and operationalize comprehensive, AI-aware incident response procedures to manage, contain, and remediate these issues efficiently.

To establish robust alerting mechanisms for AI issues that you identify, consider the following recommendations:

  * Configure actionable alerts to notify the relevant teams, based on the monitoring activities of your platform. For example, configure alerts to trigger when Model Monitoring on Agent Platform detects significant drift, skew, or prediction anomalies. Or, configure alerts to trigger when Model Armor or custom Monitoring rules flag malicious inputs or unsafe outputs.
  * Define clear notification channels, which can include Slack, email, or SMS through Pub/Sub integrations. Customize the notification channels for your alert severities and the responsible teams.



Develop and operationalize an AI-aware incident response plan. A structured incident response plan is vital to minimize any potential impacts and ensure recovery. Customize this plan to address AI-specific risks such as model tampering, incorrect predictions due to drift, prompt injection, or unsafe outputs from generative models. To create an effective plan, include the following key phases:

  * **Preparation** : Identify assets and their vulnerabilities, develop playbooks, and ensure that your teams have appropriate privileges. This phase includes the following tasks:

    * Identify critical AI assets, such as models, datasets, and specific Agent Platform resources like endpoints or Feature Store instances.
    * Identify the assets' potential failure modes or attack vectors.
    * Develop AI-specific playbooks for incidents that match your organization's threat model. For example, playbooks might include the following:

      * A model rollback that uses versioning in Model Registry.
      * An emergency retraining pipeline on Gemini Enterprise Agent Platform Managed Training.
      * The isolation of a compromised data source in BigQuery or Cloud Storage.
    * Use IAM to ensure that response teams have the necessary least-privilege access to tools that are required during an incident.

  * **Identification and triage** : Use configured alerts to detect and validate potential incidents. Establish clear criteria and thresholds for how your organization investigates or declares an AI-related incident. For detailed investigation and evidence collection, use Logging for application logs and service logs, and use Cloud Audit Logs for administrative activities and data access patterns. Security teams can use Google SecOps for deeper analyses of security telemetry.

  * **Containment** : Isolate affected AI systems or components to prevent further impact or data exfiltration. This phase might include the following tasks:

    * Disable a problematic Agent Platform endpoint.
    * Revoke specific IAM permissions.
    * Update firewall rules or Cloud Armor policies.
    * Pause a Agent Platform pipeline that's misbehaving.
  * **Eradication** : Identify and remove the root cause of the incident. This phase might include the following tasks:

    * Patch the vulnerable code in a custom model container.
    * Remove the identified malicious backdoors from a model.
    * Sanitize the poisoned data before you initiate a secure retraining job on Gemini Enterprise Agent Platform Managed Training.
    * Update any insecure configurations.
    * Refine the input validation logic to block specific prompt-injection techniques.
  * **Recovery and secure redeployment** : Restore the affected AI systems to a known good and secure operational state. This phase might include the following tasks:

    * Deploy a previously validated and trusted model version from Model Registry.
    * Ensure that you find and apply all of the security patches for vulnerabilities that might be present in your code or system.
    * Reset the IAM permissions to the principle of least privilege.
  * **Post-incident activity and lessons learned** : After you resolve the significant AI incidents, conduct a thorough post-incident review. This review involves all of the relevant teams, such as the AI and ML, MLOps, security, and data science teams. Understand the full lifecycle of the incident. Use these insights to refine the AI system design, update security controls, improve Monitoring configurations, and enhance the AI incident response plan and playbooks.




Integrate the AI incident response with the broader organizational frameworks, such as IT and security incident management, for a coordinated effort. To align your AI-specific incident response with your organizational frameworks, consider the following:

  * **Escalation** : Define clear paths for how you escalate significant AI incidents to central SOC, IT, legal, or relevant business units.
  * **Communication** : Use established organizational channels for all internal and external incident reports and updates.
  * **Tooling and processes** : Use existing enterprise incident management and ticketing systems for AI incidents to ensure consistent tracking and visibility.
  * **Collaboration** : Pre-define collaboration protocols between AI and ML, MLOps, data science, security, legal, and compliance teams for effective AI incident responses.



## Contributors

Authors: 

  * [Kamilla Kurta](https://www.linkedin.com/in/kamillakurta) | GenAI/ML Specialist Customer Engineer
  * [Vidhi Jain](https://www.linkedin.com/in/vidhi-jain-jpm) | Cloud Engineer, Analytics and AI
  * [Mohamed Fawzi](https://www.linkedin.com/in/fawzii) | Benelux Security and Compliance Lead
  * [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist



Other contributors: 

  * [Lauren Anthony](https://www.linkedin.com/in/lauren-a-5a778a44) | Customer Engineer, Security Specialist
  * [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect
  * [John Bacon](https://www.linkedin.com/in/johnbac/) | Partner Solutions Architect
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Mónica Carranza](https://www.linkedin.com/in/monicaecp/) | Senior Generative AI Threat Analyst
  * [Tarun Sharma](https://www.linkedin.com/in/tarun27in) | Principal Architect
  * [Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director



[ Previous arrow_back  Operational excellence  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence)

[ Next Reliability  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-26 UTC."],[],[]] 
