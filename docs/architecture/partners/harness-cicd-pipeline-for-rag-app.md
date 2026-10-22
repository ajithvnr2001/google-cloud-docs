---
url: https://docs.cloud.google.com/architecture/partners/harness-cicd-pipeline-for-rag-app/
title: Harness CI/CD pipeline for RAG applications \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:48.550961+00:00
---

# Harness CI/CD pipeline for RAG applications  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/harness-cicd-pipeline-for-rag-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Harness CI/CD pipeline for RAG applications Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-04-11 UTC

By Martin Ansong, Senior Solutions Engineer at Harness

This reference architecture describes how to implement a continuous integration (CI) and continuous deployment (CD) pipeline for a [retrieval-augmented generation (RAG) application in Google Cloud](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search). The architecture uses CI/CD products from [Harness](https://www.harness.io/products/platform) to deploy containers to Cloud Run services. Harness is a software delivery platform that offers AI-driven solutions for all phases of software delivery. Harness also offers Cloud Cost Management (CCM) for cost optimization. The architecture provides a scalable and efficient approach to deploy and manage RAG-capable generative AI applications, and helps to ensure secure, automated, and cost-effective application delivery.

The intended audience for this document includes architects, developers, and DevOps engineers who develop and manage generative AI applications.

## Architecture

The following diagram shows a CI/CD pipeline for deploying Cloud Run services for a RAG-capable generative AI application by using Harness products. The diagram is described in detail in the sections that follow.

![A RAG-capable generative AI application uses Harness products and a CI/CD pipeline to deploy Cloud Run services.](https://docs.cloud.google.com/static/architecture/images/harness-cicd-pipeline-for-rag-app-architecture.svg)![](https://docs.cloud.google.com/static/architecture/images/harness-cicd-pipeline-for-rag-app-architecture.svg)

### Components

This architecture consists of the following components:

  * **Source code management (SCM)** : The development workflow starts with a Git-based SCM repository like GitHub, [Harness Code Repository](https://developer.harness.io/docs/code-repository/get-started/overview), or [Cloud Code](https://docs.cloud.google.com/code). The repository triggers the CI/CD pipeline for new commits or merge events.
  * [**Harness Continuous Integration (CI)**](https://developer.harness.io/docs/continuous-integration/get-started/overview): This component does the following: 
    * Runs unit tests and security scans and builds the container image.
    * Pushes the built image to Google Cloud's Artifact Registry or to [Harness Artifact Registry](https://developer.harness.io/docs/artifact-registry/get-started/overview).
    * Runs integration tests in a Cloud Run development environment.
  * [**Harness Security Test Orchestration (STO)**](https://developer.harness.io/docs/security-testing-orchestration/get-started/overview): Automates and orchestrates security testing across the CI/CD pipeline. This testing includes static application security testing (SAST), dynamic application security testing (DAST), and software composition analysis (SCA).
  * [**Harness Supply Chain Security (SCS)**](https://developer.harness.io/docs/software-supply-chain-assurance/get-started/overview): This component does the following: 
    * Automatically generates software bills of material (SBOMs) to provide transparency into open-source and third-party components.
    * Implements policy-as-code to govern the use of open-source software based on factors like component name, version, supplier, and licensing attributes.
    * Generates and verifies provenance in line with [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) specifications to ensure artifact integrity.
    * Provides visibility into the usage of software components across all artifacts, deployments, and environments.
  * [**Harness Continuous Delivery (CD) & GitOps**](https://developer.harness.io/docs/continuous-delivery): This component does the following: 
    * Deploys the application progressively from development to staging and then from staging to production.
    * Uses feature flags for controlled feature rollout.
    * Implements traffic-shifting strategies like [canary](https://en.wikipedia.org/wiki/Canary_release) and [blue-green](https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment) deployments.
  * [**Harness Feature Management & Experimentation (FME)**](https://www.harness.io/products/feature-management-experimentation): This component does the following: 
    * Uses feature flags to test different versions of the software.
    * Routes a percentage of user traffic to each version dynamically.
    * Collects performance metrics for decision-making.
  * [**Cloud Run**](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run): Executes stateless frontend and backend services for the generative AI application with automatic scaling.
  * [**Harness Policy As Code**](https://developer.harness.io/docs/platform/governance/policy-as-code/harness-governance-overview/): Provides governance of pipeline components through policy enforcement, which helps to ensure security and operational compliance.
  * [**Harness Cloud Cost Management (CCM)**](https://developer.harness.io/docs/cloud-cost-management/get-started/overview): This component does the following: 
    * Monitors the cost efficiency of Google Cloud resources.
    * Detects cost anomalies and suggests optimizations.
    * Implements autoscaling policies based on cost insights.



### CI/CD workflow

The following is a typical workflow for developing and deploying applications by using the CI/CD pipeline that's shown in the preceding diagram. The step numbers in this workflow correspond to the numbers that are shown in the diagram.

  1. A triggering event from an SCM system starts the pipeline. The trigger could be a code commit or a merge action, such as a GitHub pull request.
  2. During the CI phase, the code is compiled, and unit tests are executed.

     * Harness Test Intelligence optimizes the testing process by running only the relevant tests based on the code changes. This optimization helps to reduce unnecessary testing time.
     * Security scans are also executed to ensure the integrity of the code.

The developer receives the results immediately to allow actionable improvements.

  3. The code is packaged into a container image and pushed either to Harness Artifact Registry or to Google Cloud's Artifact Registry, where it's automatically scanned.

  4. The container image is deployed to a development environment, where integration tests are conducted.

  5. The image is promoted to the staging environment for additional testing, including [chaos tests](https://en.wikipedia.org/wiki/Chaos_engineering) and load tests to ensure robustness.

  6. An approval gate is implemented before promotion to production. The approval gate helps to ensure that business processes, such as database changes or model performance, undergo proper review and approval. For example, database changes might require approval by a change advisory board (CAB).

  7. In the production environment, the application is deployed by using a canary release strategy. Traffic shifting is implemented between the old and new versions of the application. If failures occur, the application is rolled back to a stable version to minimize downtime.

  8. Feature flags are used to validate or test any features that have been released. This approach enables controlled experimentation without fully exposing new features to all users at the same time.

  9. The cost management system tracks and monitors resource utilization, detects cost anomalies, and offers recommendations for autoscaling to ensure cost-effectiveness.




## Products used

This reference architecture uses the following products:

  * Google Cloud products: 
    * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
    * [ Artifact Registry](https://cloud.google.com/artifact-registry/docs/overview): A universal package manager for all of your build artifacts and dependencies. 
    * [ Cloud Logging](https://cloud.google.com/logging): A real-time log management system with storage, search, analysis, and alerting.
    * [ Cloud Monitoring](https://cloud.google.com/monitoring): A service that provides visibility into the performance, availability, and health of your applications and infrastructure. 
  * [**Harness**](https://www.harness.io/) products: 
    * [**CI**](https://www.harness.io/products/continuous-integration): Enables automated testing, security scans, and builds of Docker images.
    * [**CD & GitOps**](https://www.harness.io/products/continuous-delivery): Enables progressive deployments through canary and blue-green deployment strategies with automated validation by using AI-driven anomaly detection.
    * [**STO**](https://www.harness.io/products/security-testing-orchestration): Automates and orchestrates security testing (including SAST, DAST, and SCA) across the CI/CD pipeline.
    * [**SCS**](https://developer.harness.io/docs/software-supply-chain-assurance/get-started/overview): Ensures the integrity and security of the software supply chain by providing visibility into open-source components, enforcing policies, and managing licenses to mitigate risks associated with dependencies.
    * [**Chaos Engineering**](https://www.harness.io/products/chaos-engineering): Conducts resilience testing through controlled failures.
    * [**CCM**](https://www.harness.io/products/cloud-cost-management): Monitors costs, detects anomalies, and provides scaling recommendations.
    * [**FME**](https://www.harness.io/products/feature-management-experimentation): Enables feature flag management, A/B testing, and comprehensive experimentation.
    * [**Harness Artifact Registry**](https://www.harness.io/products/artifact-registry): Centralizes, secures, and streamlines artifact management.



## Use cases

This architecture is ideal for the following use cases:

  * **RAG applications that require real-time AI-based retrieval** : Harness CD & GitOps ensures seamless deployment of AI models and RAG services across cloud environments.
  * **Serverless AI workflows for scalable inference** : 
    * Harness CI automates the packaging of AI models into containers, making them deployment-ready for serverless architectures like Cloud Run services.
    * Harness FME enables controlled rollout of AI model updates, ensuring seamless inference without affecting production workloads.
  * **Security and governance in AI deployments by using automated policy enforcement** : 
    * Harness STO integrates AI security testing (SAST, DAST, and SCA) into the CI/CD pipeline. This integration helps to protect the software against vulnerabilities in AI models and inference code.
    * Harness SCS enforces security policies on AI dependencies and generates SBOMs for tracking open-source and third-party components.
  * **Optimizing cloud costs with automated cost monitoring and recommendations** : Harness CCM provides cost insights to optimize the scaling of AI-based retrieval workloads.



## Design considerations

This section describes design factors, best practices, and design recommendations that you should consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, cost, and operational efficiency.

The guidance in this section isn't exhaustive. Depending on the specific requirements of your application and the Google Cloud and third-party products and features that you use, there might be additional design factors and trade-offs that you should consider.

### Security, privacy, and compliance

This section describes design considerations and recommendations to design a Harness-based CI/CD topology in Google Cloud that meets the security and compliance requirements of your workloads.

Product | Design considerations and recommendations  
---|---  
Harness Platform | 

  * Enable Harness Policies to enforce specific compliance controls.


  * Assume the Delegate role or use Workload Identity Federation to grant short term access to the Harness Google Cloud connector. For more information, see [Configure OIDC with Google Cloud's Workload Identity Federation for Harness Cloud](https://developer.harness.io/docs/continuous-integration/secure-ci/configure-oidc-gcp-wif-ci-hosted/).


  * Securely store and inject sensitive credentials into deployment pipelines by using Harness Security Managers.

  
Harness STO | Automate security scanning within the CI/CD pipeline to detect vulnerabilities early.  
Harness SCS | Enable Harness SCS and gain insights into the security posture of code repositories and artifacts. Collect evidence and enforce supply chain governance policies based on security benchmarks and SBOMs.  
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) | Implement secure secrets management for API keys and credentials.  
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) | Enable IAM policies for role-based access control (RBAC), to help ensure that only authorized users and service accounts can modify and deploy to specific environments.  
[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) | Use Workload Identity Federation instead of service account tokens. Workload Identity Federation helps you to avoid the maintenance and security burden that's associated with service account keys.  
  
### Reliability

This section describes design considerations and recommendations to enhance the reliability of your workloads and the CI/CD pipeline.

Product | Design considerations and recommendations  
---|---  
Harness Platform | Use [Harness templates](https://developer.harness.io/docs/platform/templates/template/) to standardize deployment practices and configuration across environments.  
Harness CD & GitOps | Use a [verify step](https://developer.harness.io/docs/continuous-delivery/verify/verify-deployments-with-the-verify-step/) in deployments to monitor application health and automatically roll back when anomalies are detected.  
Cloud Run | Configure [autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) in Cloud Run to handle anticipated loads.  
Cloud Logging and Cloud Monitoring | Implement proactive monitoring to detect and resolve availability issues in real time.  
  
### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build using this reference architecture.

Product | Design considerations and recommendations  
---|---  
Harness CCM | Use Harness CCM to get recommendations and automatic cost anomaly detection to optimize the cost of your cloud resources.  
Cloud Run |  When you create Cloud Run services, you specify the amount of memory and CPU to be allocated to the container instance.

  * To control costs, start with the default (minimum) CPU and memory allocations.


  * To improve performance, you can increase the allocation by configuring the CPU limit and memory limit.

For more information, see the following documentation:

  * [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits)


  * [Configure CPU limits for services](https://docs.cloud.google.com/run/docs/configuring/services/cpu)

  
  
### Operational efficiency

This section describes design considerations and recommendations for creating a CI/CD pipeline in Harness that meets the operational requirements of your workloads in Google Cloud. By applying these recommendations, you can streamline operations and ensure continuous delivery at scale.

Product | Design considerations and recommendations  
---|---  
Harness CI | 

  * Enable [Build Intelligence](https://developer.harness.io/docs/continuous-integration/use-ci/build-and-upload-artifacts/build-intelligence) to improve build times.


  * Use [Test Intelligence (TI) ](https://developer.harness.io/docs/continuous-integration/use-ci/run-tests/ti-overview)to speed up unit test cycles.


  * User [Docker layer caching (DLC)](https://developer.harness.io/docs/continuous-integration/use-ci/caching-ci-data/docker-layer-caching) to seamlessly cache Docker image layers between builds and accelerate the time to build Docker images.

  
Harness Chaos Engineering | Validate application resilience by simulating failures and high traffic conditions.  
Harness FME | Enable controlled feature rollouts and experimentation.  
Harness Platform | 

  * Automate compliant builds and deployments by using Policy As Code.


  * Automate pipeline approvals for controlled deployments.

  
[Harness DB DevOps](https://developer.harness.io/docs/database-devops/get-started/overview) | Seamlessly integrate database updates to ensure consistency and avoid breaking changes.  
[Harness Incident Response (IR)](https://www.harness.io/demo/harness-incident-response) | Use Harness IR to triage, adapt, and resolve incidents.  
Cloud Logging and Cloud Monitoring | Set up alerts and logging for proactive operational insights.  
  
## Deployment

To deploy this reference architecture, you can download and use the Terraform sample configuration that's available in a repository in [GitHub](https://github.com/harness-community/harness-rag-ci-cd). Follow the instructions in the README in the repository. The repository contains all of the necessary configurations and scripts to set up the Google Cloud topology and the CI/CD pipeline in Harness.

## What's next

  * Learn more about the [Harness products](https://developer.harness.io/docs/) that are used in this reference architecture.
  * Explore Harness [reference architectures](https://developer.harness.io/kb/reference-architectures) and best practices.
  * Learn how to build [RAG infrastructure for generative AI using Agent Platform and Vector Search](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Martin Ansong](https://www.linkedin.com/in/martin-ansong) | Senior Solutions Engineer (Harness)

Other contributors: 

  * [Abhi Das](https://www.linkedin.com/in/abhi1das) | Strategic Partnerships Manager
  * [Akash Gupta](https://www.linkedin.com/in/akashgupta1689) | ISV Partner Engineer
  * [Cedric Yao](https://www.linkedin.com/in/cedricyao) | Head of App Innovation Programs GTM
  * [Eddie Villalba](https://www.linkedin.com/in/edvilla) | Product Manager
  * [Jerome Simms](https://www.linkedin.com/in/jeromesimms) | Director, Product Management
  * [Ksenia Dudina](https://www.linkedin.com/in/ksenia-dudina) | Staff UX Designer (Harness)
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Mia Villasenor](https://www.linkedin.com/in/villasenormia) | Senior Developer Relations Engineer
  * [Morgan Joscelyn](https://www.linkedin.com/in/morganjoscelyn) | Director, Global Cloud Alliances (Harness)
  * [Nicholas Durkin](https://www.linkedin.com/in/nickdurkin) | Field CTO (Harness)
  * [Preston Holmes](https://www.linkedin.com/in/ptone) | Outbound Product Manager - App Acceleration



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-11 UTC."],[],[]] 
