---
url: https://docs.cloud.google.com/deployment-manager/docs/migrate-to-python3/
title: Migrate your templates to Python 3 \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:03.810177+00:00
---

# Migrate your templates to Python 3  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/migrate-to-python3/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Migrate your templates to Python 3 Stay organized with collections  Save and categorize content based on your preferences. 

[Starting on January 1, 2020](https://www.python.org/doc/sunset-python-2/), the Python community will no longer update, fix bugs, or patch security issues for Python 2.7. We recommend that you make sure that your Deployment Manager templates are compatible with Python 3 as soon as possible.

For an overview of the products affected by this change, including information about using the Google Cloud Python client libraries, see [Python support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset).

## Migrating your Deployment Manager templates

The syntax for Deployment Manager does not use any features specific to Python 3. In most cases, your templates should work with Python 3 without requiring code changes.

If you use [template modules](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-template-modules) such as helper scripts, you must make sure that the scripts are compatible with Python 3.

For information on porting Python 2 code to Python 3, see the [Python.org porting guide](https://docs.python.org/3/howto/pyporting.html). If you want to test whether your template is compatible with Python 3, try a test deployment with the template. If the deployment succeeds without any warnings, your template is compatible, and doesn't need changes.

If your templates have features that are incompatible with Python 3, your deployments will continue to work until June 2020. You might see one of these warnings:

  * The template is incompatible with Python 3: The template runs using Python 2, but fails with Python 3. The warning shows the Python 3 error message, so that you can debug your code.

  * The template produced different results with Python 3 and Python 2: This could be because your deployment is non-deterministic (for example, it relies on the current time or random numbers), or a template might be using a feature incompatible with Python 3. If your template is non-deterministic by design, you don't need to change it.

If your template uses a feature that is incompatible with Python 3, use the guidelines in the [Python 3 porting guide](https://docs.python.org/3/howto/pyporting.html) to update the template.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
