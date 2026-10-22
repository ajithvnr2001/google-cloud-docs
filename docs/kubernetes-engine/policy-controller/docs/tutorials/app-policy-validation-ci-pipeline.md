---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline/
title: Validate apps against company policies in a CI pipeline \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:19.750596+00:00
---

# Validate apps against company policies in a CI pipeline  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Validate apps against company policies in a CI pipeline Stay organized with collections  Save and categorize content based on your preferences. 

If your organization uses Policy Controller to manage policies across its Google Kubernetes Engine clusters, then you can validate an app's deployment configuration in its continuous integration (CI) pipeline. This tutorial demonstrates how to achieve this result. Validating your app is useful if you are a developer building a CI pipeline for an app, or a platform engineer building a CI pipeline template for multiple app teams.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce, and who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Policies are an important part of the security and compliance of an organization. Policy Controller allows your organization to manage those policies centrally and declaratively for all your clusters. As a developer, you can take advantage of the centralized and declarative nature of those policies. You can use those characteristics to validate your app against those policies as early as possible in your development workflow. Learning about policy violations in your CI pipeline instead of during the deployment has two main advantages: it lets you [shift left on security](https://docs.cloud.google.com/solutions/devops/devops-tech-shifting-left-on-security), and it tightens the feedback loop, reducing the time and cost necessary to fix those violations.

This tutorial uses Cloud Build as a CI tool and a sample GitHub repository containing policies for demonstrations.

## Resources

This tutorial uses several Kubernetes tools. This section explains what those tools are, how they interact with each other, and whether you can replace them with something else.

The tools that you use in this tutorial include the following:

  * [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview): is based on the open source project [Open Policy Agent - Gatekeeper](https://www.openpolicyagent.org/docs/latest/kubernetes-introduction/). Policy Controller enforces policies about the objects that are created in a Kubernetes cluster (for example, preventing the usage of a specific option or enforcing the usage of a specific label). Those policies are called [_constraints_](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints). Constraints are defined as [Kubernetes Custom Resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). Policy Controller is available as part of GKE, but you can use Open Policy Agent - Gatekeeper instead of Policy Controller for your implementation.

  * [GitHub](https://github.com/features): In this tutorial, we use GitHub to host the Git repositories: one for a sample app, and one that contains the constraints for Policy Controller. For simplicity, the two repositories are two different folders in a single Git repository. In reality, they would be different repositories. You can use any Git solution.

  * [Cloud Build](https://docs.cloud.google.com/build): Cloud Build is Google Cloud's CI solution. In this tutorial, we use it to run the validation tests. While the details of the implementation can vary from one CI system to another, the concepts outlined in this tutorial can be used with any container-based CI system.

  * [Kustomize](http://kustomize.io/): Kustomize is a customization tool for Kubernetes configurations. It works by taking "base" configurations and applying customizations to them. It lets you have a DRY (Don't Repeat Yourself) approach to Kubernetes configurations. With Kustomize, you keep elements that are common to all your environments in the base configurations and create customizations per environment. In this tutorial, we keep the Kustomize configurations in the app repository, and we "build" (for example, apply the customizations) the configurations in the CI pipeline. You can use the concepts outlined in this tutorial with any tool that produces Kubernetes configurations that are ready to be applied to a cluster (for example, the [helm template](https://helm.sh/docs/helm/helm_template/) command).

  * [Kpt](https://kpt.dev): Kpt is a tool to build workflows for Kubernetes configurations. Kpt lets you fetch, display, customize, update, validate, and apply Kubernetes configurations. Because it works with Git and YAML files, it is compatible with most of the existing tools of the Kubernetes ecosystem. In this tutorial, we use kpt in the CI pipeline to fetch the constraints from the anthos-config-management-samples repository, and to validate the Kubernetes configurations against those constraints.




### Pipeline

The CI pipeline we use in this tutorial is shown in the following diagram:

![CI pipeline for Policy Controller](https://docs.cloud.google.com/static/kubernetes-engine/policy-controller/docs/img/app-policy-validation-ci-pipeline.svg)

The pipeline runs in Cloud Build, and the commands are run in a directory containing a copy of the sample app repository. The pipeline starts by generating the final Kubernetes configurations with Kustomize. Next, it fetches the constraints that we want to validate against from the anthos-config-management-samples repository using kpt. Finally, it uses kpt to validate the Kubernetes configurations against those constraints. To achieve this last step, we use a specific [config function](https://catalog.kpt.dev/) called [gatekeeper](https://catalog.kpt.dev/gatekeeper/v0.2/) that performs this validation. In this tutorial, you trigger the CI pipeline manually, but in reality you would configure it to run after a `git push` to your Git repository.

## Objectives

  * Run a CI pipeline for a sample app with Cloud Build.
  * Observe that the pipeline fails because of a policy violation.
  * Modify the sample app repository to comply with the policies.
  * Run the CI pipeline again successfully.



## Costs

This tutorial uses the following billable components of Google Cloud:

  * Cloud Build
  * Google Kubernetes Engine



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

When you finish this tutorial, you can avoid continued billing by deleting the resources that you created. For more details, see the Cleaning up section.

## Before you begin

  1. Select or create a Google Cloud project. In the Google Cloud console, go to the **Manage resources** page:

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. [Enable billing for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

  3. To execute the commands listed in this tutorial, open Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  4. In Cloud Shell, run `gcloud config get-value project`.

If the command does not return the ID of the project that you just selected, configure Cloud Shell to use your project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

  5. In Cloud Shell, enable the required Cloud Build API:
         
         gcloud services enable cloudbuild.googleapis.com
         




## Validate the sample app configurations

In this section, you run a CI pipeline with Cloud Build for a sample app repository that we provide. This pipeline validates the Kubernetes configuration available in that sample app repository against constraints available in a anthos-config-management-samples repository.

To validate the app configurations:

  1. In Cloud Shell, clone the sample app repository:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-config-management-samples.git
         

  2. Run the CI pipeline with Cloud Build. Logs of the build are displayed directly in Cloud Shell.
         
         cd anthos-config-management-samples/ci-app/app-repo
         gcloud builds submit .
         

The pipeline that you run is defined in the following file.
         
         steps:
         - id: 'Prepare config'
           # This step builds the final manifests for the app
           # using kustomize and the configuration files
           # available in the repository.
           name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
           entrypoint: '/bin/sh'
           args: ['-c', 'mkdir hydrated-manifests && kubectl kustomize config/prod > hydrated-manifests/prod.yaml']
         - id: 'Download policies'
           # This step fetches the policies from the Anthos Config Management repository
           # and consolidates every resource in a single file.
           name: 'gcr.io/kpt-dev/kpt'
           entrypoint: '/bin/sh'
           args: ['-c', 'kpt pkg get https://github.com/GoogleCloudPlatform/anthos-config-management-samples.git/ci-app/acm-repo/cluster@main constraints
                           && kpt fn source constraints/ hydrated-manifests/ > hydrated-manifests/kpt-manifests.yaml']
         - id: 'Validate against policies'
           # This step validates that all resources comply with all policies.
           name: 'gcr.io/kpt-fn/gatekeeper:v0.2'
           args: ['--input', 'hydrated-manifests/kpt-manifests.yaml']

In Policy Controller, constraints are instantiations of constraint templates. Constraint templates contain the actual [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) code used to implement the constraint. The `gcr.io/kpt-fn/gatekeeper` function needs both the constraint template and constraint definitions to work. The sample policy repository contains both, but in reality they can be stored in different places. Use the `kpt pkg get` command as needed to download both constraint templates and constraints.

This tutorial uses `gcr.io/kpt-fn/gatekeeper` with Cloud Build to validate resources, but there are two other alternatives that you can use:

     * Use the [`gcr.io/kpt-fn/gatekeeper` function](https://catalog.kpt.dev/gatekeeper/v0.2/) with `kpt`:
    
    kpt fn eval hydrated-manifests/kpt-manifests.yaml --image gcr.io/kpt-fn/gatekeeper:v0.2
    

     * Use the [`gator` command-line tool](https://open-policy-agent.github.io/gatekeeper/website/docs/gator/):
    
    gator test -f hydrated-manifests/kpt-manifests.yaml
    

  3. After a few minutes, observe that the pipeline fails with the following error:
         
         [...]
         Step #2 - "Validate against policies": [error] apps/v1/Deployment/nginx-deployment : Deployment objects should have an 'owner' label indicating who created them.
         Step #2 - "Validate against policies": violatedConstraint: deployment-must-have-owner
         Finished Step #2 - "Validate against policies"
         2022/05/11 18:55:18 Step Step #2 - "Validate against policies" finished
         2022/05/11 18:55:19 status changed to "ERROR"
         ERROR
         ERROR: build step 2 "gcr.io/kpt-fn/gatekeeper:v0.2" failed: exit status 1
         2022/05/11 18:55:20 Build finished with ERROR status
         

The constraint that the configuration is violating is defined in the following file. It's a Kubernetes custom resource called `K8sRequiredLabels`.
         
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: K8sRequiredLabels
         metadata:
           name: deployment-must-have-owner
         spec:
           match:
             kinds:
               - apiGroups: ["apps"]
                 kinds: ["Deployment"]
           parameters:
             labels:
               - key: "owner"
             message: "Deployment objects should have an 'owner' label indicating who created them."

For the constraint template corresponding to this constraint, see [`requiredlabels.yaml`](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/blob/main/ci-app/acm-repo/cluster/requiredlabels.yaml) on GitHub.

  4. Build the full Kubernetes configuration yourself, and observe that the `owner` label is indeed missing. To build the configuration:
         
         kubectl kustomize config/prod
         




## Fix the app to comply with company policies

In this section, you fix the policy violation using Kustomize:

  1. In Cloud Shell, add a `commonLabels` section to the base Kustomization file:
         
         cat <<EOF >> config/base/kustomization.yaml
         commonLabels:
           owner: myself
         EOF
         

  2. Build the full Kubernetes configuration, and observe that the `owner` label is now present:
         
         kubectl kustomize config/prod
         

  3. Rerun the CI pipeline with Cloud Build:
         
         gcloud builds submit .
         

The pipeline now succeeds with the following output:
         
         [...]
         Step #2 - "Validate against policies": [RUNNING] "gcr.io/kpt-fn/gatekeeper:v0"
         Step #2 - "Validate against policies": [PASS] "gcr.io/kpt-fn/gatekeeper:v0"
         [...]
         


**Tip** : You can run and debug Cloud Build pipelines locally without having to trigger an actual build or pushing to your Git repository using [cloud- build-local](https://docs.cloud.google.com/build/docs/build-debug-locally).

## Clean up

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
