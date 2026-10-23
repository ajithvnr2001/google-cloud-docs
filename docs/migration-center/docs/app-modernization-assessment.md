---
url: https://docs.cloud.google.com/migration-center/docs/app-modernization-assessment/
title: Create an App Modernization Assessment \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:55.709965+00:00
---

# Create an App Modernization Assessment  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/app-modernization-assessment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Create an App Modernization Assessment Stay organized with collections  Save and categorize content based on your preferences. 

The **Migration Center App Modernization Assessment** (`codmod`) is an AI-powered tool that automates the modernization assessment process for your application. This page outlines the steps to install, use, and troubleshoot the `codmod` tool.

## About App Modernization Assessment

The typical modernization assessment process takes a few weeks and requires a lot of expertise. By automating this process, the `codmod` tool significantly reduces this time to a few hours.

This tool aims to provide evidence-based information about the current application's architecture, functionality, and potential blockers that might slow the transformation to the cloud.

This tool is intended for the following roles:

  * IT architects
  * Decision makers
  * Application owners



The `codmod` tool aims to expedite application transformation by providing clear visibility into the required changes, and the benefits gained from transforming the application to Google Cloud. The `codmod` is a portable CLI tool that uses Gemini to analyze source code and provides recommendations based on Google Cloud best practices.

**Note:** The `codmod` tool sends your code to Vertex AI. Your code is not used for training, and by default your code is not stored anywhere. For further reading see: [How Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

### Before you begin

The `codmod` tool requires the following prerequisites:

  * A **Linux** or **Windows** (10 or newer) workstation.
  * Access to a Google Cloud project that has the Vertex AI API enabled.
  * A gcloud CLI installation on your workstation. For more information, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).



### Pricing

The cost of using Gemini for code assessment is primarily driven by the size of the codebase, and is measured in tokens. The following table shows the costs estimates that you can expect to see based on your lines of code and the model that you choose: 

**Codebase** | **Lines of Code (LOC)** | **Estimated Cost**  
---|---|---  
**adaptive** | **2.5-flash** | **2.5-pro** | **3.5-flash** | **3.8-flash (default)**  
[Spring Petclinic](https://github.com/spring-projects/spring-petclinic) | ~6,500 | $20 | $3 | $20 | $3 | $9  
[James Project](https://github.com/apache/james-project) | ~1,000,000 | $40 | $30 | $200 | $200 | $200  
[Elasticsearch](https://github.com/elastic/elasticsearch) | ~5,000,000 | $200 | $200 | $900 | $500 | $500  
  
These values might be an overestimate because they don't take into account possible savings due to the following:

  * Reduced pricing for short queries.
  * Reduced pricing for implicit caching.
  * Committed use discounts (CUDs).



Costs for these parameters are expected to be a negligible part of the total cost, especially for larger codebases. For additional information, see [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing#gemini-2.5-pro).

### Additional information

The tool uses the Vertex AI API's advanced code understanding and analysis capabilities. For more information about the available models and their features, see [Google models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models) in the Vertex AI API documentation.

To maintain optimal performance and cost efficiency, `codmod` has a codebase size limit of approximately 6 million lines of code. For codebases exceeding this limit, we recommend dividing them into smaller, manageable parts for analysis. Analyzing smaller sections can also help in more focused assessments and potentially reduce overall processing time.

**Tip:** If you have any further questions or encounter any issues, email us at [codmod-feedback-external@google.com](mailto:codmod-feedback-external@google.com).

## Set up `codmod`

This section provides installation and authentication instructions to use the `codmod` tool.

### Install `codmod`

### Windows

Run the following command in **Windows PowerShell** to download the latest version of `codmod`:
    
    
    $version=curl.exe -s https://codmod-release.storage.googleapis.com/latest
    curl.exe -O "https://codmod-release.storage.googleapis.com/${version}/windows/amd64/codmod.exe"
    

### Linux

Run the following command to download the latest version of `codmod`:
    
    
    version=$(curl -s https://codmod-release.storage.googleapis.com/latest)
    curl -O "https://codmod-release.storage.googleapis.com/${version}/linux/amd64/codmod"
    chmod +x codmod
    

To use the `codmod` command, add the executable to path, or create an alias.

### Authenticate to Google Cloud

To use the `codmod` tool, you need a Google Cloud project.

  1. Ensure the Vertex AI API is enabled on the project in the [console](https://console.cloud.google.com/marketplace/product/google/aiplatform.googleapis.com) or using the CLI:
         
         gcloud services enable aiplatform.googleapis.com --project <project-id>
         

  2. Ensure you have `roles/aiplatform.user` role or similar on the project.

  3. To authenticate, run the following command:
         
         gcloud auth application-default login
         




Alternatively, you can use a service account and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. To learn more, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials#GAC).

## Manage the `codmod` configuration

The following sections explain how to configure `codmod` with the `codmod config` command.

### List all settings

To see all current configuration properties and their values, run the following command:
    
    
    codmod config list
    

### Set a default value for a flag

To set a default value for a property, use the `set` command. For example, to set the default project ID, run:
    
    
    codmod config set project "PROJECT_ID"
    

Replace `PROJECT_ID` with the Google Cloud project ID.

To set the default region, run:
    
    
    codmod config set region "REGION"
    

Replace `REGION` with the Google Cloud region. See the [list of available regions](https://docs.cloud.google.com/vertex-ai/docs/general/locations#available-regions). If you are unsure of which region to use, use `us-central1`.

### Get a specific value

To view the value of a single property, use the `get` command. For example, to get the configured project ID, run the following command:
    
    
    codmod config get project
    

### Unset a default value

To remove a configured default and revert to the tool's original default setting, use the `unset` command. For example, to remove the default project ID, run the following command:
    
    
    codmod config unset project
    

## Create a `codmod` assessment report

The following sections describe how to create the default assessment and how to customize it according to your needs.

### Create the default report

To create an assessment report, run the `codmod` tool with the following flags:
    
    
    codmod create -c "CODEBASE" -o "OUTPUT"
    

Replace the following:

  * `CODEBASE`: specifies the directory that contains the source code to analyze, and can be specified multiple times.
  * `OUTPUT`: specifies the path where the generated report is saved. The report is in HTML format.



You can override the default project and region with the `-p "PROJECT_ID"` and `-r "REGION"` flags, respectively.

You can also specify the following optional flags:

  * `--modelset [2.5-flash|2.5-pro|3.5-flash|3.8-flash|adaptive]`: specifies which Gemini models to use. The default value is `3.8-flash`. Adaptive provides a significant cost reduction with a potential trade-off in report quality compared to `2.5-pro`.
  * `--format <html|markdown|odt|json>`: the format used for the generated report. The default is HTML.
  * `--allow-large-codebase`: by default `codmod` will ask for confirmation before analyzing on codebases larger than 1 million lines of code - to avoid high costs. This option serves as a non-interactive confirmation. You can also enable this by default by running `codmod config set allow_large_codebase true`.
  * `--improve-fidelity`: when set, `codmod` generates sections serially instead of in parallel. This improves consistency between different sections of the final report, but requires a longer run time.
  * `--force-include <strings>`, `--force-exclude <strings>`: by default, `codmod` scans popular file extensions including Java, .NET, and Python. Use these flags to include or exclude file extensions. The argument must be a regular expression with the RE2 syntax.
  * `--experiments`: specify `--experiments=enable_pdf,enable_images` to support PDFs and images in `codmod`.
  * `--context <string>`: any additional context that you want to provide about the project. The tool takes this context into consideration when generating the report.
  * `--context-file <path>`: same as `--context` where the context is provided in the given file.
  * `--supporting-documents <path>`: specifies a directory of supporting documentation about the codebase. Files in this directory can be referenced from the context provided with the `--context` or `--context-file` flags to be included in the analysis. Supported formats include text, PDF, and images (PNG, JPG, JPEG).



### Create a full report

If you need a full analysis, create a report using the `create full` command:
    
    
    codmod create full -c "~/mycodebase/" -o "report.html"
    

### Create a report focused on data layer

If a deeper attention to the data layer is required, a report can be created with focus on this area:
    
    
    codmod create data-layer -c "CODEBASE" -o "OUTPUT"
    

### Create a report for a specific transformation intent

If you want to focus the report towards a particular modernization intent, you can use one of the following supported intents:

  * **Microsoft workload transformation** (`MICROSOFT_MODERNIZATION`): use with applications running on Microsoft OS, the assessment will focus around transformation journeys that will modernize frameworks based on .NET to use the latest version and reduce the dependencies on Microsoft licenses.
  * **Cloud to cloud workload transformation** (`CLOUD_TO_CLOUD`): use with applications running on other hyperscaler infrastructure. The assessment will focus on the recommended changes for transforming the application, such as mapping other cloud vendor services to Google Cloud services.
  * **Legacy Java transformation** (`JAVA_LEGACY_TO_MODERN`): use with applications running Java version **Java 8 or similar** , the assessment will focus on finding upgrade dependencies and areas in the code impacted from the change to **Java 21 (the current LTS)**.
  * **Legacy Java WILDFLY transformation** (`WILDFLY_LEGACY_TO_MODERN`): use with Java EE/Jakarta EE codebases running on WildFly application server versions prior to the latest. The assessment will focus on identifying upgrade dependencies and areas in the code impacted by the WildFly application server version upgrade, including changes required for API differences and compatibility.
  * **C/C++ application to Arm architecture migration** (`ARM_MIGRATION`): use with C/C++ applications to assess their readiness and the effort required to migrate from x86-based architectures to Arm-based architectures, such as Google Cloud Axion C4A VMs. The assessment focuses on identifying potential code portability issues, architecture-specific dependencies, build system modifications, and testing considerations necessary for a successful transition to Arm from Google Cloud or another CSP like AWS's Graviton instances.



To create an intent-focused report, use the `--intent` flag:
    
    
    codmod create -c "CODEBASE" -o "OUTPUT" --intent "INTENT"
    

### Create a report with additional sections

The tool supports including additional sections which are not included by default to reduce costs. The following sections are supported:

  * `files`: a structured hierarchical view of project folders and description per each folder content to help you orient yourself on the project files.
  * `classes`: a catalog of code classes with information about each class and its dependencies on other classes. The supported languages are Java and C#.



To create the additional sections, use the `--optional-sections` flag:
    
    
    codmod create -c "CODEBASE" -o "OUTPUT" --optional-sections "SECTIONS"
    

Replace `SECTIONS` with a comma-separated list of values.

### Create a custom report

If you want to explore some specific custom topics, you can create a custom report based on the context you provide using the following command:
    
    
    codmod create custom -c "CODEBASE" -o "OUTPUT" --context "CONTEXT"
    

By default, an LLM is used to expand upon the provided context and adapt it to ensure that a coherent section is generated. You can disable this behavior by specifying `--improve-context=false`.

Additional flags:

  * `--from-template <path>`: specifies a template file that defines the document structure in either text or PDF file format. `codmod` detects the structure and asks for approval to continue generating the report.
  * `--skip-template-approval`: skips the approval request when using the `--from-template` flag.



### Modify an existing report

You can create a new section in a report or modify an existing section based on an specific section. For example, you might want to focus on a particular aspect of the system's architecture, or a particular type of security vulnerability.

Commands that modify a report will require the following flags:

  * One of `--context` and `--context-file`: specify the modification request.
  * `--from-report`: specifies the path for the existing report file.
  * `--from-section`: name of the section to be used as a basis for a new section (for example "Overview", or "Architecture").



To display all the available sections in a specific report, run the following command:
    
    
    codmod list-sections --from-report "REPORT"
    

### Revise a report section

Modify an existing section by running the following command:
    
    
    codmod revise section -c "CODEBASE" --from-report "REPORT" \
      -o "REVISED_REPORT" --from-section "SECTION_NAME" \
      --context "CONTEXT"
    

**Note:** The "Summary", "Further Analysis", "Files", and "Classes" sections are not supported with the `revise section` command.

### Create a new report section

Create a new section using the following command:
    
    
    codmod create section -c "CODEBASE" --from-report "REPORT" \
      -o "REGENERATED_REPORT" --from-section "SECTION_NAME" \
      --context "CONTEXT"
    

  * The`from-section` flag in the `create section` command is optional.
  * By default an LLM is used to expand upon the provided context and adapt it to ensure a coherent section is generated. You may disable this behavior by specifying `--improve-context=false`.



Note the following:

  * `create section` and `revise section` only support the `html` report format.
  * `create section`, `revise section`, `list-sections` expect the `--from-report` flag to point to a report in the HTML format.



### Estimate assessment costs

The `codmod` tool helps you understand the cost of using the tool by letting you calculate the approximate cost of creating a report. To view your cost estimate, run the following command:
    
    
    codmod create --estimate-cost -c "CODEBASE"
    

Cost estimates are not supported for the `create section` and`create custom` commands.

### Set the verbosity level

The `codmod` verbosity is configured using the `--verbosity LEVEL` flag. The verbosity level of the logs is one of the following: `debug`, `info`, `warn`, `error`, or `none`. The default value is `warn`.

## Check and update the `codmod` CLI version

The `codmod` CLI can automatically check if a newer version is available.

### Automatic checks

Every 24 hours, the CLI polls a Cloud Storage bucket to see if a newer version of `codmod` has been released. If a newer version is found, you will see a notification message on your terminal. The message includes the new version number and a link to download the update. This process helps ensure you can stay up-to-date with the latest features, improvements, and bug fixes.

### Disable version checks

If you prefer to disable the automatic version check, you can use the `config set` command:
    
    
    codmod config set disable_version_check true
    

To re-enable the version check, set the value back to `false`:
    
    
    codmod config set disable_version_check false
    

You can view the current state of this setting and other configurations by running:
    
    
    codmod config list
    

## Command-line completion

The `codmod` CLI tool supports shell command-line completion for Bash, Zsh, Fish, and PowerShell. This feature helps you quickly type commands, flags, and arguments by pressing the `Tab` key to see and select available options.

Autocompletion offers the following benefits:

  * **Autocomplete commands and flags:** start typing a `codmod` command or flag and press `Tab` to see possible completions.
  * **Discover options:** see valid values for certain flags. For example: 
    * `codmod create --modelset [TAB]` suggests available model sets (for example, `2.0-flash`, `2.5-pro`).
    * `codmod create --format [TAB]` suggests output formats (for example, `html`, `json`, `markdown`).
    * `codmod create --intent [TAB]` suggests predefined intents.
  * **Context-aware suggestions:** completion is tailored to the command. For example: 
    * `codmod config set [TAB]` suggests the available configuration keys you can set.
    * `codmod config get [TAB]` suggests the available configuration keys you can get.
    * File path completion is only offered for flags or arguments that expect a file or directory path (for example, `--codebase`, `--output-path`). Other flags, such as `--project`, no longer suggest file names.



### Enable shell completion

Before you enable shell completion, make sure that the `codmod` command works by adding the executable to path, or by creating an alias.

To load completions for your shell, run the appropriate command. The instructions vary depending on your shell. Use the `help` command to get specific instructions:
    
    
    # For Bash
    codmod completion bash --help
    
    # For Zsh
    codmod completion zsh --help
    
    # For Fish
    codmod completion fish --help
    
    # For PowerShell
    codmod completion powershell --help
    

For example, to load Bash completion on Linux, you might add the following to your `~/.bashrc`:
    
    
    source <(codmod completion bash)
    

Make sure to restart your shell or source your profile (for example, `source ~/.bashrc`) for the changes to take effect.

## Troubleshooting

  * **Permission denied:** if you encounter a "permission denied" error, then ensure that you granted the execution permission to the `codmod` binary by running the`chmod +x codmod` command.
  * **CLI appears to hang:** analysis can take a long time, but you can typically see the progress in the progress bar in the CLI. If the progress bar remains at 0% after 15 minutes, then verify that you have sufficient quota for the relevant model. By default, `codmod` uses the `gemini-3.8-flash` model. However, this is subject to change as different modelsets use different models for different purposes.
  * **Reporting errors:** in the event of an error needing investigation, collect the debug information to assist our development team. Logs provide crucial details for troubleshooting. Run the following command to collect the logs, then zip and share the resulting archive with the team at [codmod-feedback-external@google.com](mailto:codmod-feedback-external@google.com).
        
        codmod collect-logs -o "codmod_logs.zip"
        




## Open source licenses

You can download the open source notices for dependencies of the latest version of `codmod` by running:
    
    
    version=$(curl -s https://codmod-release.storage.googleapis.com/latest)
    curl -O "https://codmod-release.storage.googleapis.com/${version}/THIRD_PARTY_NOTICES.txt"
    

## Get support and provide feedback

To help improve the quality of this product, we collect pseudoanonymized usage data. This data is handled in accordance with our privacy policy [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). You may change your preference at any time by running the following command:
    
    
    codmod config set disable_usage_reporting true
    

You can get support and provide feedback in the following ways:

  * To get support for `codmod`, click the **Support** button in the generated HTML report, or send an email to [codmod-feedback-external@google.com](mailto:codmod-feedback-external@google.com).
  * To share feedback on `codmod`, click the **Feedback** button in the generated HTML report.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
