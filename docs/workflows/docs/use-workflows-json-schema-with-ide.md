---
url: https://docs.cloud.google.com/workflows/docs/use-workflows-json-schema-with-ide/
title: Use the Workflows JSON schema in your\u00a0IDE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:49.513122+00:00
---

# Use the Workflows JSON schema in your IDE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/use-workflows-json-schema-with-ide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Use the Workflows JSON schema in your IDE Stay organized with collections  Save and categorize content based on your preferences. 

To provide syntax support when creating a workflow, you can use the Workflows JSON schema in an integrated development environment (IDE) like Visual Studio Code (VS Code) or Intellij IDEA. Syntax support includes autocompletion, validation, and inline documentation. The schema can also be integrated into your CI/CD processes.

The Workflows JSON schema is written in JSON Schema, a declarative language that lets you annotate and validate JSON documents. The [schema source](https://github.com/SchemaStore/schemastore/blob/master/src/schemas/json/workflows.json) is hosted on [SchemaStore.org](https://www.schemastore.org/json/), a repository of schemas for common JSON-based configuration files. Note that schemas from SchemaStore.org can be applied to YAML files as well.

Depending on the IDE or editor you prefer to use, you can install a plugin or apply built-in support to use the Workflows schema. The schema can be stored locally under your project root or it can be specified through its resource URL at SchemaStore.org.

**Note:** The following instructions focus on using VS Code or IntelliJ IDEA as your IDE when creating a workflow. However, there are several [IDEs or editors](https://www.schemastore.org/json/#editors) that have direct support for schemas hosted on SchemaStore.org. You might need to enable support for SchemaStore.org. Refer to the IDE-specific instructions for associating JSON schemas and for information regarding keyboard shortcuts.

## Filename format for workflow definition files

Regardless of the IDE or editor that you use, if you are using a plugin or extension to automatically apply the Workflows schema from SchemaStore.org, the filename format for your workflow definition file must be as follows:

  * `workflows.json`
  * `workflows.yaml`
  * `workflows.yml`
  * `*.workflows.json`
  * `*.workflows.yaml`
  * `*.workflows.yml`



If you are using VS Code, or if you are using built-in support to apply the Workflows schema, you can override the filename formats.

## Limitations

Syntax support through the Workflows JSON schema focuses on the autocompletion of [keywords](https://docs.cloud.google.com/workflows/docs/reference/syntax#search) that define a workflow. The schema supports autocompletion for some [standard library functions](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview), but there is limited support for dynamic variable names, expressions, and other expression helpers. The schema also assumes that a workflow is complete and does not account for any post-processing such as the combining of subworkflows.

To avoid JSON schema conflicts, we recommend that you don't use more than one extension or plugin for Workflows syntax support.

## Associate the Workflows JSON schema in VS Code

VS Code is a source code editor that runs on your desktop and is available for Windows, macOS, and Linux. It comes with built-in support for several languages and supports extensions for other languages and runtimes. To install and set up VS Code on your machine, see [Visual Studio Code](https://code.visualstudio.com/).

The following are various ways that you can associate the Workflows JSON schema in VS Code.

### Use Cloud Code to create workflows in YAML

Cloud Code is a set of IDE plugins that makes it easier to create, deploy, and integrate applications with Google Cloud.

If you're using VS Code as your IDE, you can use Cloud Code when authoring your YAML workflows and it will automatically pull the Workflows JSON schema from SchemaStore.org. To confirm that the schema is being applied as expected, create a YAML workflow in a VS Code workspace or folder, and confirm that autocompletion is occurring for Workflows keywords.

Cloud Code also supports offline Google Cloud schemas, and can be used by those who might have network or IDE restrictions. For more information, refer to the following:

  * [Install the Cloud Code for VS Code extension](https://docs.cloud.google.com/code/docs/vscode/install)
  * [Work with YAML in Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/yaml-editing)
  * [Learn more about Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/features)



### Use YAML by RedHat to create workflows in YAML

As an alternative to using the Cloud Code for VS Code extension, you can use the [YAML by RedHat extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml). This extension provides YAML language support and includes built-in Kubernetes syntax support. It automatically pulls the Workflows JSON schema from SchemaStore.org.

After installing the extension, create a YAML workflow. At the top of the file, there should be a **Google Cloud Workflows configuration file (workflows.json)** link. If you click the link, the Workflows JSON schema opens in the VS Code editor.

### Override the filename formats

When using either Cloud Code or YAML by RedHat to create workflows in YAML, you can override the default filename formats that the Workflows schema is applied against. You must specify a mapping in the `settings.json` file. Settings are written as JSON and you can review and edit this file directly by [opening it in the VS Code editor](https://code.visualstudio.com/docs/getstarted/settings#_creating-user-and-workspace-settings).

For example, if you are using the Cloud Code for VS Code extension, you can map a filename format under the property `cloudcode.yaml.schemas`:
    
    
    {
        "cloudcode.yaml.schemas": {
            "https://json.schemastore.org/workflows.json": [
                "GLOB_PATTERN.yaml",
                "my-special-workflow.yaml"
            ]
        }
    }

Or, if you are using the YAML by RedHat extension, map the filename format under the property `yaml.schemas`:
    
    
    {
        "yaml.schemas": {
            "https://json.schemastore.org/workflows.json": [
                "GLOB_PATTERN.yaml",
                "my-special-workflow.yaml"
            ]
        }
    }

The schemas on the left are applied to the glob patterns on the right; each schema is associated with multiple globs using a JSON array. Your schema must be a relative path and not an absolute path. Your schema can be local or online.

### Use built-in support to create workflows in JSON

You can use built-in support in VS Code to associate the Workflows JSON schema by specifying the mapping in the `settings.json` file, under the property `json.schemas`. You can review and edit this file directly by [opening it in the VS Code editor](https://code.visualstudio.com/docs/getstarted/settings#_creating-user-and-workspace-settings).

For example, to pull the Workflows JSON schema from SchemaStore.org:
    
    
    {
        "json.schemas": [
            {
                "description": "SchemaStore.org",
                "fileMatch": [
                    "workflows.json",
                    "*.workflows.json"
                ],
                "url": "https://json.schemastore.org/workflows.json"
             }
        ]
    }

The schemas on the left are applied to the glob patterns on the right; a schema is associated with multiple globs using a JSON array. Your schema must be a relative path and not an absolute path. Your schema can be local or online.

You can override the filename format. For example:
    
    
    {
        "json.schemas": [
            {
                "description": "Workflows schema",
                "fileMatch": [
                    "GLOB_PATTERN.json",
                    "FILE_NAME.json"
                ],
                "url": "https://json.schemastore.org/workflows.json"
            }
        ]
    }

For more information, see [Editing JSON with Visual Studio Code](https://code.visualstudio.com/Docs/languages/json).

## Associate the Workflows JSON schema in IntelliJ IDEA

IntelliJ IDEA is a cross-platform IDE for Java Virtual Machine languages. Other languages are supported through plugins. To install and set up IntelliJ IDEA on your machine, see [Install IntelliJ IDEA](https://www.jetbrains.com/help/idea/installation-guide.html).

The following are various ways that you can associate the Workflows JSON schema in IntelliJ IDEA.

### Use Cloud Code to create workflows in YAML or JSON

Cloud Code is a set of IDE plugins that makes it easier to create, deploy, and integrate applications with Google Cloud.

If you're using IntelliJ as your IDE, you can use Cloud Code when authoring your workflows in either YAML or JSON and it will automatically pull the Workflows JSON schema from SchemaStore.org. Cloud Code also supports offline Google Cloud schemas, and can be used by those who might have network or IDE restrictions. For more information, refer to the following:

  * [Install the Cloud Code for IntelliJ plugin](https://docs.cloud.google.com/code/docs/intellij/install)
  * [Work with YAML in Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/yaml-editing)
  * [Learn more about Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/features)



### Use built-in support to create workflows in YAML or JSON

IntelliJ IDEA can automatically download and use schemas from SchemaStore.org. You can download the Workflows JSON schema and store it under the project root or specify the URL of the resource so IntelliJ IDEA can download the schema automatically. To map the schema, follow the instructions to [configure a custom JSON schema](https://www.jetbrains.com/help/idea/json.html#ws_json_schema_add_custom).

By default, [automatic downloads of schemas from SchemaStore.org](https://www.jetbrains.com/help/idea/json.html#ws_json_schema_store_enable_auto_download) are enabled and the default filename patterns are validated against the schema.

To override the default file patterns, after navigating to **JSON Schema Mappings** through the **Settings** dialog, do the following:

  1. In the **Name** field, type **Workflows schema**.
  2. In the **Schema file or URL** field, type **https://json.schemastore.org/workflows.json**.
  3. In the **Schema version** list, select **JSON Schema version 7**.
  4. Add a **File path pattern** of your choosing.



### Map the schema through `jsonSchema.xml`

IntelliJ IDEA Community Edition source code is available through <https://github.com/JetBrains/intellij-community>.

You can map the Workflows JSON schema for the IntelliJ IDEA editor by adding an entry to [jsonSchemas.xml](https://github.com/JetBrains/intellij-community/blob/master/.idea/jsonSchemas.xml).

## Add Workflows syntax validation to your CI/CD processes

Adding syntax validation to your continuous integration, delivery, and deployment (CI/CD) processes helps to reduce errors during integration, testing, delivery, and deployment.

**Note:** Google is not responsible for any third-party tools or issues arising from their use.

For example, you can validate data against the Workflows JSON schema by using the [ajv-cli](https://www.npmjs.com/package/ajv-cli) tool. Note that when installing the tool, also install [ajv-formats](https://ajv.js.org/packages/ajv-formats.html). For example:
    
    
    npm install -g ajv-cli ajv-formats

Other tools that might be useful:

  * [MegaLinter v8r](https://megalinter.io/latest/descriptors/yaml_v8r/)—MegaLinter is an open source tool for CI/CD workflows; v8r checks the validity of JSON/YAML files if they have a matching schema defined on SchemaStore.org.
  * [JSON validators](https://json-schema.org/tools?query=&sortBy=name&sortOrder=ascending&groupBy=toolingTypes&licenses=&languages=&drafts=&toolingTypes=validator&environments=)—JSON validation tools categorized by programming language or development platform.



## What's next

  * Google Cloud Blog: [Workflows gets an updated JSON Schema](https://cloud.google.com/blog/products/application-development/integrated-workflows-inside-your-ide-of-choice-help-you-develop)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
