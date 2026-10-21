---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/app-armor-profile/
title: Using a custom AppArmor profile \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:35.380985+00:00
---

# Using a custom AppArmor profile  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/app-armor-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using a custom AppArmor profile

[AppArmor](https://apparmor.net/) lets a system administrator restrict capabilities of a deployed container by using custom profiles. In some cases, you might have to apply a custom profile to your deployed container to customize its capabilities.

To customize the AppArmor profile:

  1. Create the profile on the cluster where you are deploying your migrated container. See the [AppArmor](https://apparmor.net/) documentation for more information.

  2. Edit the `deployment_spec.yaml` file to add the `HC_APPARMOR_PROFILE` environment variable with the name of the AppArmor profile:
         
         spec:
           containers:
           - image: gcr.io/my-project/my-container:v1.0.0
             name: my-container
             env:
             - name: HC_APPARMOR_PROFILE
               value: "apparmor-profile-name"
             securityContext:
               privileged: true
         ...
         

See [Reviewing generated deployment files](https://docs.cloud.google.com/migrate/containers/docs/review-deployment-files) for more on editing `deployment_spec.yaml`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
