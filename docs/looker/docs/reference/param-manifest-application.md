---
url: https://docs.cloud.google.com/looker/docs/reference/param-manifest-application/
title: application \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:17.048003+00:00
---

# application  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-manifest-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  application Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    application: application_name {
      label: "Application Label" 
      url: "application_url" 
      file: "application_file_path" 
      sri_hash: "SRI_hash_value" 
      mount_points: {
        dashboard_vis: yes | no
        dashboard_tile: yes | no
        standalone: yes | no
      }
      entitlements: {
        local_storage: yes | no
        navigation: yes | no
        new_window: yes | no
        new_window_external_urls: ["url1", "url2", ...]
        use_form_submit: yes | no
        use_embeds: yes | no
        use_downloads: yes | no
        use_iframes: yes | no
        use_clipboard: yes | no
        core_api_methods: ["api_method1", "api_method2", ...]
        external_api_urls: ["api_url1", "api_url2", ...]
        oauth2_urls: ["oauth2_url1", "oauth2_url2", ...]
        global_user_attributes: ["user_attribute1", "user_attribute2", ...]
        scoped_user_attributes: ["user_attribute1", "user_attribute2", ...]
      }
    }
    

Hierarchy [Manifest File](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) `application` |  Default Value None Accepts A name for the application and subparameters to define it Special Rules The `application` must have a `url` or a `file` parameter, but not both   
---|---  
  
## Definition

The `application` parameter defines an application for Looker's [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework). Once an extension is added to a project, Looker users with [appropriate permissions](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions) can see the extension in the location that is defined by the `mount_points` parameter. If the `mount_points` parameter is not specified, the extension is listed in the **Applications** section of the Looker menu.

The `application` parameter has the following subparameters:

  * `label`
  * `url`
  * `file`
  * `sri_hash`
  * `mount_points`
  * `entitlements`



> The application must have either a `url` parameter or a `file` parameter, but not both.

### `label`

Specifies the name of the application that is displayed to the user in the **Applications** section of the main menu. The `label` can be localized if you are [localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization).

### `url`

The `url` parameter is used for development purposes only, and should point to a development server running on the developer's machine. For example:
    
    
    url: "http://localhost:8080/bundle.js"
    

After development, you can [drag the file into the Looker IDE](https://docs.cloud.google.com/looker/docs/other-project-files#adding_data_files) and then use the `file` parameter to point to the file.

### `file`

Specifies the path to a JavaScript file (with a `.js` extension) that defines the application. The path is relative to the project root. For example, this `file` parameter points to the `bundle.js` file in the `apps` directory of the LookML project:
    
    
    file: "apps/bundle.js"
    

### `sri_hash`

Specifies a [Subresource Integrity (SRI)](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) hash for JavaScript verification purposes. It can be used with either the `file` or the `url` parameter. The `sri_hash` value should _not_ include the `sha384-` prefix.

The `sri_hash` is ignored if the `url` specifies a development server.

### `mount_points`

The `mount_points` parameter determines where in the Looker UI the extension will be listed and made available to the user, and whether the extension will provide its own data. [Extensions that are intended to run in a dashboard tile](https://docs.cloud.google.com/looker/docs/extension-framework-building-tile-extensions) require `mount_points` to be specified. If `mount_points` is not specified, the extension will be listed in the **Applications** section of the Looker menu. Multiple `mount_points` are allowed.

Parameter | Description | Example  
---|---|---  
`dashboard_vis` | When enabled, the extension will appear in the [visualization list of an Explore](https://docs.cloud.google.com/looker/docs/creating-visualizations#choosing_a_visualization_type), where the extension can be selected and [saved as a dashboard tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore). When the dashboard is run, the dashboard will execute the query that is associated with the tile and make the data available to the extension. This is similar to how [custom visualizations](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization) work. The primary difference between a custom visualization and an extension running in a dashboard tile that has `dashboard_vis` enabled is that the extension may make [Looker API](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) calls.  | `dashboard_vis: yes`  
`dashboard_tile` | When enabled, the extension will appear in the [**Extensions** panel](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_extensions) that is displayed when a user is editing a dashboard and selects the **Extensions** option after clicking the **Add** button. This type of extension is responsible for retrieving its own data.  | `dashboard_tile: yes`  
`standalone` | Specifies whether the extension will be listed in the **Applications** section of the Looker menu. If the `mount_points` parameter is not specified, `standalone: yes` is the default setting for the extension.  | `standalone: yes`  
  
### `entitlements`

The `entitlements` parameter specifies the resources that the extension can access. The extension will not be able to access the resources unless it is listed in `entitlements`.

> An extension application must specify entitlements; the application won't run without them.

The `entitlements` parameter includes the following subparameters. If a subparameter is not included, then by default the extension is not allowed access to that entitlement.

Parameter | Description | Example  
---|---|---  
`local_storage` | Specifies whether the extension is allowed to access local storage.  | `local_storage: yes`  
`navigation` | Specifies whether the extension is allowed to navigate to a different page in Looker.  | `navigation: yes`  
`new_window` | Specifies whether the extension is allowed to open a new browser window or tab.  | `new_window: yes`  
`new_window_external_urls` | A comma-separated list of URLs or partial URLs for which an extension may open a new window. This entitlement requires the `new_window` entitlement. You can include wildcard characters such as `*` for subdomains and paths.  | `new_window_external_urls: ["https://www.gmail.com"]`  
`use_form_submit` | Specifies whether the extension is allowed to submit forms. Looker components that use HTML forms will require `use_form_submit: yes` to work properly.  | `use_form_submit: yes`  
`use_embeds` | Specifies whether the extension is allowed to use the [Looker Embed SDK](https://docs.cloud.google.com/looker/docs/embed-sdk-intro).  | `use_embeds: yes`  
`use_downloads` |  Added 21.6  Specifies whether the extension is allowed to download files.  | `use_downloads: yes`  
`use_iframes` |  Added 21.6  Specifies whether the extension is allowed to create an iframe.  | `use_iframes: yes`  
`use_clipboard` |  Added 21.8  Specifies whether the extension is allowed to write to the system clipboard. For security purposes, extensions are not allowed to read from the system clipboard.  | `use_clipboard: yes`  
`core_api_methods` | A comma-separated list of [Looker API](https://docs.cloud.google.com/looker/docs/api-getting-started) methods that the extension uses.  | `core_api_methods: ["run_inline_query", "lookml_model_explore", "all_lookml_models"]`  
`external_api_urls` | A comma-separated list of URLs for external APIs that the extension uses. As shown in the example, you can include wildcard characters such as `*`. Starting in Looker 21.6, extensions that make direct use of `fetch` or `XHR.open` JavaScript calls (as opposed to using the `extensionSDK.fetchProxy` or `extensionSDK.serverProxy` API calls) must include the URLs in the list.  | `external_api_urls: ["http://example.com:3000", "https://*.googleapis.com"]`  
`oauth2_urls` | A comma-separated list of URLs for OAuth 2.0 authentication and code exchange that the extension uses.  | `oauth2_urls: ["https://accounts.google.com/o/oauth2/v2/auth"]`  
`global_user_attributes` | A comma-separated list of system-wide user attributes that the extension uses.  | `global_user_attributes: ["company", "department"]`  
`scoped_user_attributes` | A comma-separated list of extension-specific user attributes that the extension uses.  | `scoped_user_attributes: ["first_name", "last_name"]`  
  
## Example

The following is the `application` parameter from the project manifest file for Looker's [kitchen sink extension example](https://github.com/looker-open-source/extension-examples/tree/main/react/typescript/kitchensink):
    
    
    application: kitchensink {
      label: "Kitchen sink"
      url: "http://localhost:8080/bundle.js"
      entitlements: {
        local_storage: yes
        navigation: yes
        new_window: yes
        use_form_submit: yes
        use_embeds: yes
        core_api_methods: ["all_connections","search_folders", "run_inline_query", "me", "all_looks", "run_look"]
        external_api_urls: ["http://127.0.0.1:3000", "http://localhost:3000", "https://&lowast;.googleapis.com", "https://&lowast;.github.com", "https://REPLACE_ME.auth0.com"]
        oauth2_urls: ["https://accounts.google.com/o/oauth2/v2/auth", "https://github.com/login/oauth/authorize", "https://dev-5eqts7im.auth0.com/authorize", "https://dev-5eqts7im.auth0.com/login/oauth/token", "https://github.com/login/oauth/access_token"]
        scoped_user_attributes: ["user_value"]
        global_user_attributes: ["locale"]
      }
    }
    

For additional examples, see Looker's [extension-examples repository](https://github.com/looker-open-source/extension-examples).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
