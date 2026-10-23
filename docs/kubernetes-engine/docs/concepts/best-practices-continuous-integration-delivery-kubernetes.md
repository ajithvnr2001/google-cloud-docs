---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes/
title: Best practices for continuous integration and delivery to Google Kubernetes Engine \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:50.270275+00:00
---

# Best practices for continuous integration and delivery to Google Kubernetes Engine  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for continuous integration and delivery to Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide describes a set of best practices for continuous integration and continuous delivery (CI/CD) to Google Kubernetes Engine (GKE). These practices cover a wide range of topics, from source control to deployment strategies. These best practices are specific to GKE and general CI/CD best practices still apply. For more information, see [DevOps tech: Continuous integration](https://docs.cloud.google.com/architecture/devops/devops-tech-continuous-integration) and [DevOps tech: Continuous delivery](https://docs.cloud.google.com/architecture/devops/devops-tech-continuous-delivery).

For a summarized checklist of all the GKE best practices, see the Checklist summary at the bottom of this guide.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## Continuous integration

[Continuous integration (CI)](https://docs.cloud.google.com/architecture/devops/devops-tech-continuous-integration) is a practice in which developers integrate all their code changes back into a main branch as often as possible. It's meant to allow for faster failures by exposing issues as early as possible in the process. CI pipelines are usually triggered by developers pushing code changes. The pipeline involves steps to validate those changes such as linting, testing, and building. A CI pipeline typically produces an artifact that you can deploy in later stages of the deployment process.

**Best practices** :

Create pipelines that enable rapid iteration.  
Test your container images.  
Establish security early.  


### Create pipelines that enable rapid iteration

The time between when a developer makes a code change and when you have a running version of the application should be as short as possible. This speed is especially important during development on feature branches that involve fast iteration by developers. Ideally, your CI pipelines should run in less than 10 minutes. If that isn't possible, then create two types of CI pipelines:

  * **Rapid pipelines** : These pipelines typically run in 10 minutes or less. These pipelines are for feature branches and are not meant to be comprehensive. Rapid pipelines can potentially result in unstable artifacts.

  * **Full pipelines** : These pipelines can take longer than 10 minutes to run, and they run more comprehensive tests and checks. Full pipelines run on merge or pull requests, and commits to the main branch.




### Test your container images

As part of your CI pipelines, ensure that you run all the required tests on your code and build artifacts. These tests should include unit, functional, integration, and load or performance testing.

It's also important to test the structure of your built container images. Testing the structure ensures that all commands run as you expect them to inside of your container. Testing also lets you check that specific files are in the correct location and have the correct content.

To test your container images, you can use the [Container Structure Tests](https://github.com/GoogleContainerTools/container-structure-test) framework.

### Establish security early in pipelines

Have security checks and balances as early as possible in the development life cycle. By finding security risks before you build artifacts or deploy, you can reduce the time and cost spent to address these risks.

To help achieve early detection, you can implement the following security measures in your pipelines:

  * **Require that subject matter experts review any code integrated into your production repository**.

  * **Implement linting and static code analysis early in your pipeline**. This testing helps you find weaknesses such as not escaping inputs, accepting raw input data for SQL queries, or vulnerabilities in your code.

  * **Scan your built container image for vulnerabilities with[vulnerability scanning](https://docs.cloud.google.com/artifact-registry/docs/analysis)**.

  * **Prevent images that contain vulnerabilities from being deployed to your clusters, by using[Binary Authorization](https://docs.cloud.google.com/binary-authorization)**. Binary Authorization requires an [GKE Enterprise subscription](https://cloud.google.com/binary-authorization/pricing). To provide you with higher confidence in the produced images, Binary Authorization also lets you require [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations) by different entities or systems. For example, these attestations could include the following:

    * Passed vulnerability scan
    * Passed QA testing
    * Sign off from product owner



## Continuous delivery

[Continuous delivery (CD)](https://docs.cloud.google.com/architecture/devops/devops-tech-deployment-automation) lets you release code at any time. CD operates on the artifact produced by CI pipelines. CD pipelines can run for much longer than CI pipelines, especially if you're using more elaborate deployment strategies such as [blue-green deployments](https://wikipedia.org/wiki/Blue-green_deployment).

**Best practices** :

Use GitOps methodology.  
Promote, rather than rebuild containers.  
Consider using more advanced deployment options.  
Separate clusters for different environments.  
Keep your pre-production environments as close as possible to production.  
Prepare for failures in production.  


### Use GitOps methodology

GitOps is the concept of declarative infrastructure stored in Git repositories and the CI/CD tools to deploy that infrastructure to your environment. When you use a GitOps methodology, you ensure that all changes to your applications and clusters are stored in source repositories and are always accessible.

Using GitOps methodologies provides you with the following advantages:

  * You can review changes before they are deployed through merge or pull requests.
  * You have a single location that you can use to refer back to the state of your applications and clusters at any point in time.
  * Snapshots of your clusters and applications make it easier to recover when there are failures.



Some common tools used for declarative infrastructure are [Terraform](https://docs.cloud.google.com/docs/terraform) by Hashicorp and [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) by Google Cloud. For hands-on practice managing infrastructure with GitOps and other tools, try the [Managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/architecture/managing-infrastructure-as-code) tutorial. To learn how to manage applications in GitOps style, try the [GitOps-style continuous delivery with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build).

### Promote, rather than rebuild container images

Container images shouldn't be rebuilt as they pass through the different stages of a CI/CD pipeline. Rebuilding can introduce minor differences across code branches. These differences can cause your application to fail in production or cause the accidental addition of untested code in the production container image. To ensure that the container image you tested is the container image you deploy, it's best to build once and promote along your environments. This advice assumes that you are keeping environment-specific configuration separate from packages.

### Consider using more advanced deployment and testing patterns

GKE offers you the flexibility to deploy and test your applications using several patterns. The deployment pattern you choose largely depends on your business goals. For example, you might need to deploy changes without any downtime or deploy changes to an environment or a subset of users before you make a feature generally available.

Some of the different deployment patterns available for you include the following:

  * **Recreating a deployment** : You fully scale down the existing application version before you scale up the new application version.

  * **Rolling update deployment** : You update a subset of running application instances instead of updating all the running application instances at one time. Then you progressively update more of the running application instances until they are all updated.

  * **Blue-green deployment** : You deploy an additional parallel set of instances to your existing production instances with an upgraded version of your application. You switch over traffic to the new instances when you are ready to deploy.




### Separate clusters for different environments

Separation of environments is an important consideration for any deployment target. Ideally, you should have separate clusters for each of the following environments:

  * **Development environment** : This environment is where your developers deploy applications for testing and experimentation. These deployments require integration with other parts of the application or system (for example, a database). The clusters for this environment typically have fewer gates, and developers have greater control over their cluster configuration.

  * **Pre-production environments (Staging or QA)** : These environments should resemble the production environment as closely as possible. They're used to perform large-scale tests of changes like integration, load, performance, or regression tests.

  * **Production environment** : This environment is where your production workloads and user-facing applications and services run.




### Keep pre-production environments close to production

Ideally, pre-production clusters are identical to production clusters, but for cost purposes pre-production clusters can be scaled down replicas. Keeping the clusters similar ensures that any testing is done on the same or similar conditions to what's in production. Parity between pre-production and production clusters also reduces the probability of unexpected failures due to environmental differences when you deploy to production.

Declarative infrastructure and GitOps help you to achieve a closer parity of your environments because you can more easily duplicate the configuration of your underlying cluster. To ensure your environments have similar conditions for policies and configurations, you can also use tools like [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview).

### Prepare for failures in production

No amount of testing can guarantee the proper behavior of your application in production. Failures can be caused by edge cases with data that weren't considered or access patterns by your users that weren't tested. It's important to monitor your application in production and have automated rollback and deployment mechanisms so you can quickly react to and fix bugs or outages. Using more robust deployment strategies allows you to reduce the impact of issues and affect fewer of your end users when issues arise in production.

## Checklist summary

The following table summarizes the tasks that we recommend when you use a CI/CD pipeline in GKE:

Area | Tasks  
---|---  
Continuous integration |  Create pipelines that enable rapid iteration. Test your container images. Establish security early in pipelines.  
Continuous delivery |  Use GitOps methodology.  Promote, rather than rebuild containers. Consider using more advanced deployment and testing patterns.  Separate clusters for different environments. Keep pre-production environments close to production. Prepare for failures in production.  
  
## What's next

  * Learn about [Best practices for enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy).
  * Learn more about [CI/CD on Google Cloud](https://docs.cloud.google.com/docs/ci-cd).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
