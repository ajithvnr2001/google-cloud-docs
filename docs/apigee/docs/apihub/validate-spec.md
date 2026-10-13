---
url: https://docs.cloud.google.com/apigee/docs/apihub/validate-spec/
title: Validate API specs using the specification linter \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:33.382387+00:00
---

# Validate API specs using the specification linter  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/validate-spec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Validate API specs using the specification linter Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

API hub provides the **Specification linter** add-on which validates your API's OpenAPI specification. Soon after you add an OpenAPI specification to your API version, the linter validates the specification, and reports the findings in the Google Cloud console.

**Note:** The **Specification linter** add-on is enabled by default in API hub. You can disable the linter add-on anytime. See Disable specification validation.

## Style guide

A style guide is a set of rules against which API hub validates an OpenAPI specification. API hub uses a default style guide for validating the OpenAPI specifications. For the default style guide rules, see [OpenAPI Rules](https://meta.stoplight.io/docs/spectral/4dec24461f3af-open-api-rules).

**Note:** To add your own custom rules, you must create a new style guide that extends the default style guide. After adding your custom rules in the new style guide, you must upload the new style guide in API hub.

### Upload a new style guide

### Console

To upload a new style guide, do the following steps:

  1. Create a new style by extending the default style guide. For more information, see [Create a ruleset](https://meta.stoplight.io/docs/spectral/01baf06bdd05a-create-a-ruleset). 
  2. In the Google Cloud console, go to the **API hub > Add-on management** page. 

  3. Locate the **Specification linter** card, and then click **Manage**.
  4. In the **Specification linter** pane, click **Upload new style guide**.
  5. Browse to the new style guide that you want to upload, and then click **Open**. 

The style guide that you selected is uploaded to API hub. 

  6. Click **Close**.



### REST API

To upload a new style guide for linting, issue a `PATCH` request to the following API:

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/plugins/standard-linter/styleGuide?update_mask=contents`

For more information about the API, see [UpdateStyleGuide](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.plugins/updateStyleGuide).

The following example shows the API call to upload a style guide.
    
    
    curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"name":"projects/test-project-1/locations/us-central1/plugins/standard-linter/styleGuide",
    "contents":{  "contents": "ZXh0ZW5kczogWyJzcGVjdHJhbDpvYXMiXQo=",
      "mimeType": "text/yaml"}}' \ 
    -X PATCH \
    https://apihub.googleapis.com/v1/projects/test-project-1/locations/us-central1/plugins/standard-linter/styleGuide?update_mask=contents  
    

### Download the default style guide

To download the default style guide used by API hub for linting, do the following steps:

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

  2. Locate the **Specification linter** card, and then click **Manage**.
  3. In the **Specification linter** pane, click **Download default style guide**.
  4. Click **Close**.



### Download the latest style guide

### Console

To download the style guide that is currently used by API hub for linting, do the following steps:

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

  2. Locate the **Specification linter** card, and then click **Manage**.
  3. In the **Specification linter** pane, click **Download latest style guide**.
  4. Click **Close**.



### REST API

To download the style guide that is currently used by API hub for linting, issue a `GET` request to the following API:

`https://apihub.googleapis.com/v1/projects/PROJECT/locations/LOCATION/plugins/standard-linter/styleGuide:contents`

For more information about the API, see [GetStyleGuide](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.plugins/getStyleGuide).

The following example shows the API call to download the current style guide.
    
    
    curl -X \
    GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      https://apihub.googleapis.com/v1/projects/test-project-1/locations/us-central1/plugins/standard-linter/styleGuide:contents
    

## Disable specification linter

By default, the **Specification linter** add-on is enabled in API hub. If you don't want to validate your API specifications, you can disable the linter add-on. To disable the linter add-on, do the following steps:

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

[Go to Add-on management](https://console.cloud.google.com/apigee/api-hub/add-on-management)

  2. Locate the **Specification linter** card and click **Manage**. 

The **Specification linter** pane appears. 

To disable the add-on, click **Disable specification linter** , and then click **Disable** in the confirmation dialog.

  3. Click **Save**.



### Limitations

The following limitations apply when creating and uploading custom style guides:

  * **No URLs in`extends` property**: Style guides can't contain URLs. Ensure that you don't include any URLs in the `extends` property of your ruleset when creating and uploading a style guide. For example, the following property construction might cause the upload to fail: `extends: [spectral:oas", "https://mystyle.com/"]`.
  * **`functionsDir` not allowed**: The `functionsDir` property is not allowed in custom style guides. Spectral style guides with JavaScript will not be executed by API hub during the linting process. 

As a workaround, if you require the use of a custom style guide with JavaScript functions, perform the following steps:

    1. Run [Spectral](https://stoplight.io/open-source/spectral) outside of API hub using your custom style guide.
    2. Update the linting results in the `Lint` attribute of the specification file in API hub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
