---
url: https://docs.cloud.google.com/cluster-toolkit/docs/getting-support/
title: Get support \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:00.713168+00:00
---

# Get support  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/getting-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Resources ](https://docs.cloud.google.com/cluster-toolkit/docs/release-notes)



Send feedback 

#  Get support Stay organized with collections  Save and categorize content based on your preferences. 

You can find various support options for Cluster Toolkit to help ensure the smooth operation of your high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads. These resources include Google's official channels and the open-source community.

## Get a Google support package

Google Cloud offers different support packages to meet different needs, such as 24-7 coverage, phone support, and access to a technical support manager. For more information, see [Cloud Customer Care](https://docs.cloud.google.com/support).

Support for Cluster Toolkit is offered under the Standard support package and higher. To learn more about the different levels of support, review [Cloud Customer Care](https://docs.cloud.google.com/support).

If you're not sure whether you have a paid technical support package, check your Cloud Customer Care console:

[Go to Support](https://console.cloud.google.com/support)

### Open a support case

If you have paid support, you can open a support case from the Cloud Customer Care console. To open a support case, review [Customer Care procedures](https://docs.cloud.google.com/support/docs/customer-care-procedures).

To open a support case for Cluster Toolkit from the console, you need to specify Compute Engine as the product, and then on the following page, select Cluster Toolkit from the category list.

## Get support from the community

Because Cluster Toolkit is an open source project, you can also get support from the following forums.

### Ask a question on the GitHub discussions page

The central discussion forum for Cluster Toolkit users and community developers is the [Cluster Toolkit GitHub discussions page](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions). From this page, you can review past discussions, ask questions to other Cluster Toolkit users and developers, and stay up to date with the Cluster Toolkit community.

### Open an issue using the GitHub issue tracker

For issues with the [`gcluster` CLI](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) and Cluster Toolkit modules, you can open an issue on [GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/issues) to report a bug or request a new feature.

For issues related to certain [community modules](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules), you can seek support directly from the partner developers. If available, you can find this information in the Support section of the module README. For example:

  * [SchedMD](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/scheduler/schedmd-slurm-gcp-v6-controller#support)

  * [DDN](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/file-system/DDN-EXAScaler#support)




## Recommendations for efficient support

To allow the Cloud Customer Care team or Cluster Toolkit engineering to respond expeditiously to your issue, include as much of the following information as is possible in a report:

  1. A clear and concise description of what the problem is.
  2. Steps to reproduce the behavior.
  3. A description of what you expected to happen.
  4. A description of what actually happened.
  5. The output of `gcluster --version`, which has Cluster Toolkit and Terraform version information.
  6. Attach a copy of the blueprint (YAML file) used.
  7. Any output logs or screenshots that might be useful.
  8. Terraform Provider versions 
     * Navigate to the deployment group folder where the issue occurred. The deployment group folder uses the following naming convention: `DEPLOYMENT_NAME/GROUP_NAME`. For example, if the deployment name is `hpc-small` and the group name is `primary`, you would access the folder as follows: `cd ./hpc-small/primary`. In that folder call `terraform version` and provide the output.
  9. Information about the environment where the `./gcluster` command was run. This includes the following: 
     * Operating system: [such as macOS, ubuntu]
     * Shell (To find this, run `ps -p $$`): [bash, zsh, …]
     * Output of `go version`:
     * Output of `gcloud --version`:



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
