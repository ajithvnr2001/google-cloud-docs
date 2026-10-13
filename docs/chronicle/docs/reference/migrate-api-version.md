---
url: https://docs.cloud.google.com/chronicle/docs/reference/migrate-api-version/
title: Migrate Chronicle API versions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:02.073738+00:00
---

# Migrate Chronicle API versions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/migrate-api-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate Chronicle API versions

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how to migrate your integrations to a new version of the Chronicle API. It covers endpoint updates and potential request and response differences, and provides best practices for a smooth transition.

## Migrate your endpoint and requests

As the Chronicle API evolves, transitioning to newer versions ensures access to the latest features, improvements, and long-term support.

  1. Replace the existing version segment `/{OLD_VERSION}/` in your endpoint paths with the new version segment `/{NEW_VERSION}/`.

**Example:**

Replace the existing version path with the new version path:

     * `{OLD_VERSION}` path:

`https://<region>-chronicle.googleapis.com/{OLD_VERSION}/`  
`projects/<project>/locations/<location>/instances/<instance>/...`

     * `{NEW_VERSION}` path:

`https://<region>-chronicle.googleapis.com/{NEW_VERSION}/`  
`projects/<project>/locations/<location>/instances/<instance>/...`

**Note:** Ensure you are using the correct `<region>` for your instance. For details, see the regional [Service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#service-endpoint).
  2. Compare the API reference documentation for the _specific endpoints_ you use and note any changes.

     1. Go to the **Chronicle API REST reference:** <https://cloud.google.com/chronicle/docs/reference/rest>

     2. For each method you use, open the API reference documentation for both the existing and new versions.

     3. Compare each method's parameters, request bodies, and response schemas.

The new API version may structure requests and responses differently for some endpoints. Look for these potential differences:

        * Changes to field names
        * Deprecation of fields
        * Modifications to data types or formats
        * New required or optional parameters
     4. Check for field-level restrictions. The new API version may not include all the fields or features from the existing version.

     5. Update your code to the new version based on your findings.

**Example:**

When you migrate the `findUdmFieldValues` method, compare its documentation details for the existing version `{OLD_VERSION}` with the details for the new version `{NEW_VERSION}`.

For example, compare the following references, where `{OLD_VERSION}` is `v1alpha` and `{NEW_VERSION}` is `v1beta`. In this case, `pageSize` is a deprecated field that only the `v1alpha` version uses:

     * [https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/findUdmFieldValues](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances/findUdmFieldValues)
     * [https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/findUdmFieldValues](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances/findUdmFieldValues)



## Migration best practices

  * **Test thoroughly:** Before updating your production environment, test your API calls against the new version endpoints in a development or staging environment.
  * **Update code:** Modify your application code to handle any changes identified in the API reference comparison.
  * **Monitor:** After migration, monitor your applications for any unexpected behavior or errors related to the API interactions.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
