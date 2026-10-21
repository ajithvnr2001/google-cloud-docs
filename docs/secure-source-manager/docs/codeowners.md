---
url: https://docs.cloud.google.com/secure-source-manager/docs/codeowners/
title: Manage pull request approvals with CODEOWNERS \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:44.275701+00:00
---

# Manage pull request approvals with CODEOWNERS  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/codeowners/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Manage pull request approvals with CODEOWNERS Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes the structure, syntax, and implementation of the `CODEOWNERS` feature, which lets you flexibly control Pull Request (PR) approval requirements.

## Introduction

The Secure Source Manager `CODEOWNERS` feature uses files in your codebase to set file-level approvers. This offers more fine-grained control than other branch rules because you can assign specific owners to specific files and define independent sets of approvers.

The `CODEOWNERS` feature offers the following capabilities:

  * Define users that can approve pull requests for files, directories, and branches.
  * Configure different sets of code owners to protect different branches.
  * Ensure that changes to files are reviewed by designated owners.



## Enabling Code Owner Review

To activate and enforce `CODEOWNERS` rules, branch protection administrators must update the [**Branch rules**](https://docs.cloud.google.com/secure-source-manager/docs/configure-branch-protection) in your repository settings to **Require Code Owner Review on Pull Requests**. Select this option in the branch rule settings. If this setting is **off** , the system ignores `CODEOWNERS` files for merges to the target branch. If you select this option, the system blocks pushes and merges to the branch until code owners review and approve the pull requests.

**Note:** Other settings, such as **N Reviewers Required** or **N Approvers Required** , are independent and additional requirements. If you are both a code owner and have the `repositories.approvePullRequests` permission, you can fulfill both requirements with a single review.

## CODEOWNERS File Location and Precedence

Secure Source Manager supports two options for defining `CODEOWNERS` files:

  1. **Nested files** : `CODEOWNERS` files in any directory **except** for the `.securesourcemanager` directory. Nested `CODEOWNERS` files affect only their own directory (including sub-directories), and file paths within them must be specified relative to the directory where the `CODEOWNERS` file is located. This is the recommended approach for most use cases.

  2. **Single dedicated file** : If you need to distinguish Secure Source Manager's `CODEOWNERS` file from other `CODEOWNERS` files used by other tools (for example, `.gitlab/CODEOWNERS`), you can use a single file located at `.securesourcemanager/CODEOWNERS` in your repository root. If this file exists, Secure Source Manager ignores all other CODEOWNERS files in the same branch, including nested ones. The `.securesourcemanager` directory is only recognized in the repository root.




## Interaction with Pull Requests and Approvals

When a pull request is created, or when its source branch is updated with new commits, the system uses only `CODEOWNERS` files from the base branch (the branch you are merging into) to determine approval requirements. The system ignores changes to `CODEOWNERS` files within the pushing code for that verification.

## CODEOWNERS syntax and structure

A `CODEOWNERS` file consists of comments, rule lines, and section markers. Comments begin with `#` and are ignored by the system.

### Rule line format

The standard format for a rule line is:

`[BRANCH_GLOB] PATH_GLOB [OWNERS...]`

Where:

  * `BRANCH_GLOB`: An optional glob pattern that specifies which branches the rule applies to. If you don't specify a branch glob, the rule applies to any branch the `CODEOWNERS` file is checked into (if the branch has `CODEOWNERS` enabled in its branch rules). For example:

    * `main` matches only the `main` branch.
    * `dev-*` matches branches beginning with `dev-`.
    * `*-glob` matches branches ending with `-glob`.
    * `my-*-glob` matches branches such as `my-feat-glob`.
**Tip:** While a CODEOWNERS file guards only its own branch, maintaining differing CODEOWNERS contents across branches can lead to merge conflicts. By using the branch field, you can use the same CODEOWNERS contents in every branch, while still setting branch-specific code owners.
  * `PATH_GLOB`: A required glob pattern that specifies which file paths the rule applies to. Secure Source Manager's syntax is based on [`gitignore` patterns](https://git-scm.com/docs/gitignore#_pattern_format).

    * If a pattern contains no `/`, or only contains `/` as a trailing character, it is a glob that matches in **any directory**. 
      * `*.js` matches JavaScript files anywhere.
      * `build/` matches directories named `build` anywhere.
    * If a pattern contains `/` anywhere other than the end, it is treated as a path relative to the `CODEOWNERS` file's location. 
      * `docs/*` matches files under `docs/` relative to the `CODEOWNERS` file.
      * `/*.js` matches JavaScript files in the same directory as the CODEOWNERS file, but not nested JavaScript files.
    * A pattern ending in `/` only matches directories and their contents recursively. For example, `build-*/` matches directories such as `build-app/` and `build-tool/` anywhere.
    * If using `.securesourcemanager/CODEOWNERS`, paths are relative to the repository root.
  * `OWNERS`: An optional list of owner email addresses, separated by spaces. If omitted, this rule acts as a path exclusion.

**Note:** You must specify individual user email addresses in `CODEOWNERS` files. Google Groups are not supported for defining owners.



### Branch-specific ownership

The optional `BRANCH_GLOB` field at the beginning of a rule line lets you implement branch-specific code owner controls.

  * If you don't specify a `BRANCH_GLOB` at the beginning of the rule, the rule applies to all branches.
  * The system ignores any line with a branch glob that does not match the current branch.



### Syntax fundamentals

  * **Field interpretation** : Fields are space-separated. 
    * Fields containing `@` are identified as owner email addresses.
    * If one field without `@` precedes owner email addresses, it's treated as `PATH_GLOB`. For example, in `*.js user@example.com`, `*.js` is the `PATH_GLOB`.
    * If two fields without `@` precede owner email addresses, the first is `BRANCH_GLOB` and the second is `PATH_GLOB`. For example, in `main *.js user@example.com`, `main` is `BRANCH_GLOB` and `*.js` is `PATH_GLOB`.
    * The same logic applies if no owners are specified: one field is `PATH_GLOB`, and two fields are `BRANCH_GLOB PATH_GLOB`.
  * **Glob-style syntax** : Secure Source Manager uses the standard glob-style (`.gitignore`-style) syntax for path expressions.
  * **Wildcard character details** : 
    * `**` matches any sequence of characters, including `/`.
    * `*` matches any sequence of characters, except `/`.
    * `?` matches any single character, except `/`.
  * **Case sensitivity** : `CODEOWNERS` files are case sensitive.
  * **Owner identification** : The system identifies owners by email address. The `@` character distinguishes owner fields.
  * In owner email addresses, only `space` and `backslash` need escaping.
  * **Reserved characters** : The system reserves the following characters. You must backslash-escape (`\`) them in branch and path expressions: `[`, `]`, ` `, `@`, `*`, `?`, `\`, `{`, `}`, and `!`.
  * If `**` is mixed with non-slash characters, the system treats it as a regular wildcard. For example, `/**/*.py` matches any depth Python file, `/**.py` is treated like `/*.py` and matches only files in the root directory.



### Sections for multiple approval sets

Using `[Section]` lines groups rules into independent required approvals. This is useful for requiring reviews from distinct teams, for example, Security or QA.

  * **Section definition** : Use a line in the format `[Section Name]` (use any natural language name).
  * **Approval count** : A section can include an optional suffix `[<approverCount>]` to specify an approval count other than 1. A count of `0` signifies optional owners. For example, you can use this to display experts on particular files for informational purposes without requiring their review.
  * **Section termination** : A section applies to all rules following it until the next section begins.
  * **Unsectioned rules** : The system treats rules that appear before any `[Section]` definition as a single unified section, requiring one approval by default.
  * **Consolidation** : The system treats sections with the same case-insensitive name, even across multiple nested `CODEOWNERS` files, as a single unified section, following standard precedence rules.



### Path exclusion

To exclude specific paths from a previous broader clause, set zero owners for the path. If you define a rule without any owners, the system removes any owners for that path set by previous rules, and the path does not require owner approvals.

Directory matches only work if they end in `/` or they contain no wildcards in the final part.

For example, `*.py` won't match a hidden directory `.py/`; `*.py/` will.

### Conflict resolution and precedence

If a `.securesourcemanager/CODEOWNERS` file exists, all other `CODEOWNERS` files are ignored. If a path is matched by two different lines in the same section, only the last line will apply. If the lines are in different sections, both will apply.

The system uses a location-based precedence rule for nested files:

  * Rules in a deeper-nested (more local) `CODEOWNERS` file override matching rules in a more shallow file.
  * The root directory `CODEOWNERS` file always has the lowest precedence.



### Example CODEOWNERS file

The following is an example `CODEOWNERS` file, demonstrating `CODEOWNERS` syntax:
    
    
    # Un-sectioned rules; 1 approve required from any of owners of last matching line.
    # Format: [BRANCH_GLOB] PATH_GLOB [OWNERS...]
    
    # Make repo-admin the owner of all files of the current branch.
    *   repo-admin@example.com      # No slash prefix; matches in sub-dirs too.
    /**/* repo-admin@example.com      # Slash-prefix equivalent of prior line.
    
    # Match all py files (including sub-dirs). Note repo-admin must be re-added.
    *.py  repo-admin@example.com python-owner@example.com
    
    # With repo-admin not included here, repo-admin no longer owns README.
    /README.md readme-owner@example.com
    
    /scratchpad.txt             # Can also override a path to have zero owners (path exclusion).
    
    # Branch-specific syntax.
    # Note that since un-sectioned rules are independent of sectioned rules,
    # the above [Section] rules will still apply to this branch if they
    # aren't modified to add e.g. `main ` as a prefix.
    dev-* *             # Remove all owners reqs on dev branches.
    dev-* /experimental/ exp-owner@example.com   # dev-specific owners.
    
    # Make repo admin own all CODEOWNERS files, regardless of any prior rules.
    CODEOWNERS repo-admin@example.com
    
    # Section; 1 approval required *in addition* to owners outside this section.
    [Security Team]
    /secure-directory/ security-expert@example.com security-reviewer@example.com
    /**/*secure\ me* security-expert@example.com security-reviewer@example.com
    
    # Section w/ req approval count of 2 instead of 1.
    [Doc Team][2]
    /docs doc-expert@example.com doc-reviewer@example.com
    *.md doc-expert@example.com doc-reviewer@example.com
    

### Compatibility with other source code managers

Secure Source Manager provides a syntax that is familiar and portable with other Source Code Managers. The Secure Source Manager `CODEOWNERS` syntax is compatible with the GitHub `CODEOWNERS` syntax, and partially compatible with the GitLab `CODEOWNERS` syntax, including sectional approval counts like `[Section Name][2]`.

The Secure Source Manager implementation of `CODEOWNERS` does not support the GitLab `!path` syntax for path negation. For information on path negation in Secure Source Manager, see Path Exclusion. Secure Source Manager also doesn't support default owners in section headers—for example, `[Section Name] @owner1 @owner2`.

## Validation and Error Handling

When viewing a `CODEOWNERS` file, the UI displays its status, and line-level warnings or information (for example, lines not matching this branch). Highlighted line numbers or lines can be hovered over to view additional details.

### Enforcement

A presubmit guard enforces the syntax error check on any branch where you enable the code owners branch rule. This prevents you from accidentally checking in broken `CODEOWNERS` files.

### Syntax Error Handling

Presubmit checks only run on branches where **Require Code Owner Review on Pull Requests** is enabled. If a syntactically invalid `CODEOWNERS` file is committed to a branch, and code owner review is later enabled for that branch, the system handles errors gracefully:

  * The system ignores lines that cannot be parsed into a section definition, rule line, or comment format.
  * If an approval count is negative, the system treats it as 0.
  * The system continues to parse and apply any valid lines as usual.



## What's next

  * [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview)
  * [Configure branch protection](https://docs.cloud.google.com/secure-source-manager/docs/configure-branch-protection)
  * [Work with issues and pull requests](https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests)
  * [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
