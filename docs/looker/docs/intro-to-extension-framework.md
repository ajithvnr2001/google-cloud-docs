---
url: https://docs.cloud.google.com/looker/docs/intro-to-extension-framework/
title: Looker extension framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:51.853410+00:00
---

# Looker extension framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/intro-to-extension-framework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker extension framework Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 22.20, to address potential [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) violations, there is a new, enhanced loading mechanism for the Looker extension framework. For more information, see the [Admin settings - Extension Framework](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) documentation page.

The Looker extension framework is a development framework that significantly reduces the effort and complexity of building custom JavaScript data applications and tools, such as:

  * Internal platform applications for your company
  * External platforms for your customers, such as customer portals for [Embedded Analytics applications](https://looker.com/product/embedded-analytics) built with data in Looker
  * Targeted internal tools
  * Applications for embedding in external applications



Current examples of Looker extensions that are available on the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) include the Looker [Data Dictionary](https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary) and the [LookML Diagram](https://docs.cloud.google.com/looker/docs/lookml-diagram-using).

## Why use the extension framework?

Some parts of building web applications are easy and fun, while others are obviously more time-consuming and not exactly fun. The extension framework helps you by streamlining many of these not-so-fun tasks.

The extension framework takes care of some of the more tedious aspects of building a web application so that you can focus on starting development right away. Custom applications and tools created with the extension framework can be accessed from within Looker, allowing Looker to handle the following kinds of functions, such as:

  * [Authentication](https://docs.cloud.google.com/looker/docs/admin-settings-authentication) — Lets you use Looker's existing authentication options for sign-in (such as [password login](https://docs.cloud.google.com/looker/docs/admin-settings-authentication-password), [LDAP](https://docs.cloud.google.com/looker/docs/admin-settings-authentication-ldap), [SAML](https://docs.cloud.google.com/looker/docs/admin-settings-authentication-saml), and [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-settings-authentication-oidc)).
  * [Access control and permission management](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management).
  * [API access](https://docs.cloud.google.com/looker/docs/api-getting-started) — Lets you use other common developer resources, such as third-party API endpoints, within Looker.



## Extension framework features

The Looker extension framework includes the following features:

  * The [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk), which provides functions for [Looker public API access](https://docs.cloud.google.com/looker/docs/api-getting-started) and for interacting within the Looker environment.
  * [Looker components](https://components.looker.com/), a library of prebuilt React UI components you can use in your extensions.
  * The [Embed SDK](https://docs.cloud.google.com/looker/docs/embed-sdk), a library you can use to embed dashboards, Looks, and Explores in your extension. See the [kitchen sink extension](https://github.com/looker-open-source/extension-examples/tree/main/react/typescript/kitchensink) for example code. You can also use the Embed SDK to embed your extension into third-party applications. Cookies must be enabled in the browser when you're embedding Explores, Looks, or dashboards into an extension.
  * The [`create-looker-extension` utility](https://github.com/looker-open-source/create-looker-extension), which creates a basic extension that includes all the necessary extension files and dependencies, and you can use as a starting point to build upon.
  * Our [Looker extension framework examples](https://github.com/looker-open-source/extension-examples) repository, which includes templates and sample extensions to assist you in getting started quickly.
  * The ability to access third-party API endpoints and add third-party data to your extension.
  * The ability to create full-screen extensions within Looker. Full-screen extensions can be used for internal or external platform applications.

In a full-screen extension, you can prevent a set of users from navigating to other parts of Looker from your extension by adding users to an Extensions Only user group. You can also remove the Looker navigation bar by replacing `/extensions` with `/spartan` in the extension URL.

  * The ability to [configure an access key](https://github.com/looker-open-source/extension-examples/tree/main/react/typescript/access-key-demo) for your extension so that users must enter a key to run the extension. This is useful if you want to charge for your extension, but you should use standard Looker permissions to gate access to those who should never be able to access an extension.

  * Starting in Looker 24.0, extensions can be [developed to run in a tile in dashboards](https://docs.cloud.google.com/looker/docs/extension-framework-building-tile-extensions). Extensions that support being run as a tile or visualization can be [added while the dashboard is in edit mode](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_extensions) or [saved to a dashboard as a visualization from an Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu). Extensions can also be configured as tiles in [LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards).




## Extension framework requirements

To develop using the Looker extension framework:

  * You will need LookML developer permissions to your instance.
  * Your Looker admin must enable the [**Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) feature.
  * We recommend familiarity with JavaScript or TypeScript.
  * We recommend development in [React](https://reactjs.org/), although there is an [extension SDK for raw JavaScript](https://www.npmjs.com/package/@looker/extension-sdk).



In order to run inside of Looker, every extension, regardless of its function, must include the following elements inside of Looker:

  * A [LookML project](https://docs.cloud.google.com/looker/docs/lookml-project-files) that meets these requirements:

    * Includes a [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files)
    * Includes a [project manifest file](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files)
    * Is [connected to a Git repository](https://docs.cloud.google.com/looker/docs/setting-up-git-connection)
  * The LookML model file needs a [`connection` parameter](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) that points to a valid [database connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) on your instance.

  * The project manifest file requires an [`application` parameter](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application). The `application` parameter gives the extension a label, tells Looker where to find the extension JavaScript, and provides a list of entitlements for the extension. Entitlements define the Looker resources that the extension can access. The extension won't be able to access a Looker resource unless that resource is listed in the entitlements.

**Note:** Starting in Looker 24.0, the [`application` parameter](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application) includes the [`mount_points` subparameter](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#mount_points), which determines where in the Looker UI the extension will be listed and made available to the user, and whether the extension will provide its own data. [Extensions that are intended to run in a dashboard tile](https://docs.cloud.google.com/looker/docs/extension-framework-building-tile-extensions) require `mount_points` to be specified in the `application` parameter.

The following is an example project manifest file with an `application` parameter:
        
        project_name: "super_duper_extension"
          application: super_duper_extension {
            label: "Super Duper Extension"
            url: "http://localhost:8080/dist/bundle.js"
            mount_points: {
              standalone: no
            }
            entitlements: {
              local_storage: no
              navigation: no
              new_window: no
              new_window_external_urls: []
              use_form_submit: yes
              use_embeds: no
              use_downloads: no
              core_api_methods: []
              external_api_urls: []
              oauth2_urls: []
              scoped_user_attributes: []
              global_user_attributes: []
            }
          }
        

For details, see the [`application` parameter](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application) documentation page.




## Getting started developing with the Looker extension framework

The easiest way to get started is to first generate a new starter extension from a template, and then customize and add functionality to that starter. This ensures that all configuration and packaging is correct, which can be difficult to do by hand. See the [Building a Looker extension](https://docs.cloud.google.com/looker/docs/extension-intro-to-building) documentation page for instructions on how to create a new Looker project for your extension and generate a starter extension.

For more customized or advanced templates, you can browse the [Looker Extension Framework Examples repository](https://github.com/looker-open-source/extension-examples). Any extension in that repository can be cloned and repurposed as a starting point for your project.

Once you have created a basic extension and verified that everything is working, you can begin to add additional functionality and customizations:

  * You can see a list of common use cases with example code on the [Extension framework React and JavaScript code examples](https://docs.cloud.google.com/looker/docs/extension-framework-react-and-js-code-examples) documentation page.

  * Reference the [Looker UI Components](https://looker-open-source.github.io/components/latest/) site to use our components library for rapid UI and layout development.

  * The [Looker Extension Kitchensink Template](https://github.com/looker-open-source/extension-examples/tree/main/react/typescript/kitchensink) is an extension that provides examples of a large variety of extension functionality. You can use this template as an encyclopedia or a reference guide, but not as a starting point or an actual template. We recommend that you use our extension generator or clone one of the more basic examples to begin.

  * Examples of extensions that can be used as dashboard tiles are also available. The [tile visualization extension](https://github.com/looker-open-source/extension-examples/tree/main/react/javascript/tile-visualization) shows how to build a custom visualization using the extension framework. The [tile sdk extension](https://github.com/looker-open-source/extension-examples/tree/main/react/javascript/tile-sdk) shows the available API methods that are specific to tile extensions.




## Uninstalling or removing extensions

To completely remove an extension framework application from the list of applications in the Looker UI, you must remove the extension's definition from the defining LookML project. Deleting a project that doesn't define the extension won't remove the extension from the UI.

To uninstall or remove an extension, follow these steps:

  1. Identify the LookML project that defines the extension.

**Tip:** You can identify the defining LookML project by inspecting the extension's URL in the Looker UI. The URL follows the format `<your_looker_domain>/extensions/project_name::application_id`. For example, in the URL `https://mycompany.looker.com/extensions/my_extension_project::my_extension_id`, the defining LookML project is `my_extension_project` and the extension ID is `my_extension_id`.
  2. Navigate to **Develop** > **Projects** as a Looker admin, and click the name of the identified project to open it.

  3. Remove the extension from the project:

     * **To remove the extension while keeping the LookML project:** Open the project's manifest file (`manifest.lkml`), and locate the `application` block that corresponds to the extension ID (for example, `application: my_extension_id { ... }`). Delete the entire `application` block, save the changes, commit the changes, and deploy them to production.
     * **To remove the extension by deleting the entire project:** If the LookML project is no longer needed, you can delete the project permanently. For instructions on deleting a project, see the [Accessing and editing project information](https://docs.cloud.google.com/looker/docs/manage-projects#deleting_a_project) documentation page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
