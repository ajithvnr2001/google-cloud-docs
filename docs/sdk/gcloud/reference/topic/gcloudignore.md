---
url: https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore/
title: gcloud topic gcloudignore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:53:00.172605+00:00
---

# gcloud topic gcloudignore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud topic gcloudignore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud topic gcloudignore - reference for `.gcloudignore` files 
DESCRIPTION
     Several commands in `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` involve uploading the contents of a directory to Google Cloud to host or build. In many cases, you will not want to upload certain files (i.e., "ignore" them). 

If there is a file called `.gcloudignore` `within the top-level directory being uploaded`, the files that it specifies (see "SYNTAX") will be ignored. 

Gcloud commands may generate a .gcloudignore file; see the individual command help page for details. 

The following `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` commands respect the `.gcloudignore` file: 

  * `[gcloud app deploy](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy)`
  * `[gcloud alpha app migrate-to-run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app/migrate-to-run)`
  * `[gcloud beta app migrate-to-run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/migrate-to-run)`
    * Note: If you add `app.yaml` to the `.gcloudignore` file, the above commands will fail. 
  * `[gcloud functions deploy](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy)`
  * `[gcloud builds submit](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit)`
  * `gcloud composer environments storage {dags, data, plugins} import`
  * `gcloud container builds submit`
  * `[gcloud run deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy)`
  * `[gcloud run jobs deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/deploy)`
  * `[gcloud run worker-pools deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy)`
  * `[gcloud alpha deploy releases create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deploy/releases/create)`
  * `[gcloud beta deploy releases create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deploy/releases/create)`
  * `[gcloud deploy releases create](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create)`
  * `[gcloud infra-manager deployments apply](https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply)`
  * `[gcloud infra-manager previews create](https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create)`
  * `[gcloud alpha functions local deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/local/deploy)`
  * `[gcloud alpha run jobs deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/deploy)`
  * `[gcloud beta run jobs deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/jobs/deploy)`
  * `[gcloud alpha run worker-pools deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/worker-pools/deploy)`
  * `[gcloud beta run worker-pools deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/worker-pools/deploy)`
  * `[gcloud alpha run instances dev sync](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/instances/dev/sync)`
  * `gcloud beta run instances dev sync`

To globally disable `.gcloudignore` parsing (including default file-ignore behavior), run: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) gcloudignore/enabled false

The default content of the generated `.gcloudignore` file, which can be overridden with `--ignore-file`, is as follows: 
    
    
    .gcloudignore
    .git
    .gitignore

EXAMPLES
     This `.gcloudignore` would prevent the upload of the `node_modules/` directory and any files ending in `~`: 
    
    
    /node_modules/
    *~

This `.gcloudignore` (similar to the one generated when Git files are present) would prevent the upload of the `.gcloudignore` file, the `.git` directory, and any files in ignored in the `.gitignore` file: 
    
    
    .gcloudignore
    # If you would like to upload your .git directory, .gitignore file or
    # files from your .gitignore file, remove the corresponding line below:
    .git
    .gitignore
    #!include:.gitignore

SYNTAX
     The syntax of `.gcloudignore` borrows heavily from that of `.gitignore`; see <https://git-scm.com/docs/gitignore> or `man gitignore` for a full reference. 

Each line in a `.gcloudignore` is one of the following: 

  * `pattern`: a pattern specifies file names to ignore (or explicitly include) in the upload. If multiple patterns match the file name, the last matching pattern takes precedence. 
  * `comment`: comments begin with `#` and are ignored (see "ADVANCED TOPICS" for an exception). If you want to include a `#` at the beginning of a pattern, you must escape it: `\#`. 
  * `blank line`: A blank line is ignored and useful for readability. 



Some example patterns follow; see the full reference (<https://git-scm.com/docs/gitignore> or `man gitignore`) for details. 

To ignore any file named `foo`, and any file in the root of the upload directory named `bar`: 
    
    
    foo
    /bar

To ignore any file starting with `foo`, ending with `bar`, or starting with `baz` and ending with `qux`: 
    
    
    foo*
    *bar
    baz*qux

To explicitly include any file named `foo` (useful if `foo` was excluded earlier in the file) and ignore a file named `!bar`: 
    
    
    !foo
    \!bar

To ignore any directory `foo` and all its contents (though not a file `foo`), any file `baz`, and the directory `qux` and all its contents: 
    
    
    foo/
    **/baz
    qux/**

ADVANCED TOPICS
     In order to ignore files specified in the gitignore file, there is a special comment syntax: 
    
    
    #!include:.gitignore

This will insert the content of a `.gitignore`-style file named `.gitignore` at the point of the include line. It does not recurse (that is, the included file `cannot` `#!include` another file) and cannot be anywhere but the top-level directory to be uploaded. 

To display files that will be uploaded run: 
    
    
    gcloud meta list-files-for-upload

NOTES
     These variants are also available: 
    
    
    [gcloud alpha topic gcloudignore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/gcloudignore)
    
    
    [gcloud beta topic gcloudignore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/gcloudignore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
