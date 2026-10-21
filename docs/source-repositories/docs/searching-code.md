---
url: https://docs.cloud.google.com/source-repositories/docs/searching-code/
title: Searching code \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:38.533714+00:00
---

# Searching code  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/searching-code/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Searching code Stay organized with collections  Save and categorize content based on your preferences. 

You can search for specific files or code snippets by using the search box located at the top of the Google Cloud console.

![Search box](https://docs.cloud.google.com/static/source-repositories/docs/images/search-box.png)

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

All searches use [RE2 regular expressions](https://github.com/google/re2/wiki/Syntax) by default. If you don't want to use regular expressions, enclose your search in double quotation marks ( " ). For example:
    
    
    foo() # Parentheses are treated as part of a regular expression. Matches 'food'.
    "foo()" # Treats the parentheses as literals. Doesn't match 'food'.
    

**Note:** If you use a search filter, such as `file`, don't enclose the filter in quotes. For example, use `file:abd.xyz` not `file:"abc.xyz"`.

## Setting search scope

The **Scope** drop-down list to the left of the search box lets you restrict your search scope to one of the following, depending on your location in the source repository interface:

  * **Everything** : Searches all repositories where you have access.
  * **This Project** : Searches all repositories in the current project.
  * **The Repository** : Searches the current repository.
  * **This Directory** : Searches the current directory.



## Searching for files

You can search for a file in several ways. For example, you can use the `file` filter to search for a file by using its path. For example:
    
    
    file:main
    

The following filters return the same results as the `file` filter:

  * `filepath`
  * `f`
  * `path`



You can also search for a file name by typing its name and extension. For example:
    
    
    main\.java
    

**Note:** The preceding example escapes the period (`\.`). This is required because searches use RE2 regular expressions by default.

## Searching file contents

You can restrict your search to the contents of a file by using the `content` filter. For example, the following query looks for the term `main` in the contents of all Java files. It does not search for instances where a path contains the term `main`.
    
    
    lang:java content:main
    

## Searching by language

To restrict your search results to a specific language, use the `language` or `lang` filter. For example, the following search restricts the search results to the Java language:
    
    
    helloworld language:java
    

You can also use the `file` filter, as shown in the following example:
    
    
    file:\.java
    

Remember that searches use regular expressions by default. As a result, the following search doesn't work:
    
    
    *.java
    

Instead, try the following searches:
    
    
    \.java
    lang:java
    

## Enabling case-sensitive searches

You can make your search case-sensitive by using the `case` filter. For example, the following search returns only results that match the term `HelloWorld`. It excludes results where the case doesn't match, such as `helloWorld` or `helloworld`.
    
    
    case:yes HelloWorld
    

## Searching for classes

To search for a specific class, use the `class` keyword. For example, the following search returns all classes with the term `Main`.
    
    
    class:Main
    

## Searching for functions

Use the `function` or `func` filters to search for a specific function. For example, the following search returns all functions with the term `main`.
    
    
    function:main
    

## Excluding terms

To exclude a term from search results, prepend the `-` character to the term you want to exclude. For example, the following search returns all functions with the term `main`, but excludes matches found in C++ files.
    
    
    function:main -lang:cpp
    

## Escaping characters

By default, searches use [RE2 regular expressions](https://github.com/google/re2/wiki/Syntax). To escape characters so they aren't treated as part of a regular expression, use the `\` character. For example, the following example searches for the term `main.java`.
    
    
    main\.java
    

## Searching for literals

Enclose your search terms in double quotation marks (`"`) to perform a literal search. For example, the following example searches for the term `main.java`.
    
    
    "main.java"
    

## Searching for symbols

To search for a specific symbol, use the `symbol` keyword. For example, the following search returns all immutable classes and functions.
    
    
    symbol:immutable
    

## Using the AND operator

You can search for multiple terms by using the `AND` operator. This operator returns results only when the terms on both sides of the operator are true. For example, the following search returns Python files that contain the term `server`.
    
    
    server AND lang:python
    

A search for multiple terms uses `AND` implicitly. For example, you could write the preceding example as follows:
    
    
    server lang:python
    

## Using the OR operator

The `OR` operator returns a result if it matches an expression on either side of the keyword. For example, the following search returns files that contain the term `hello` or the term `world`.
    
    
    hello OR world
    

## Grouping search terms

You can group multiple search terms together using parentheses (`(` and `)`). For example:
    
    
    (hello OR world) AND lang:java
    

You can also nest multiple groups. For example:
    
    
    ((Strings OR StringBuilder) AND lang:java) OR (std AND lang:cpp)
    

## Previewing search results

A search query might have multiple results in the same file. For example:
    
    
    lang:java function:foo
    

This search looks for Java files that have a `foo` function. These files might contain more than one reference to this function, however. In these situations, the search result for that file contains a **View all matches in this file** link. Click this link to open a preview pane that displays the contents of this file.

Use the preview pane to quickly preview multiple results at once while still keeping the rest of your search results in view.

## Search reference

The following tables contain the search filters and operators discussed in the preceding section.

### Search filters

The following table lists the filters you can use when searching code.

Filter | Other options | Description | Example  
---|---|---|---  
case:yes |  | Make the search case sensitive. By default, searches are not case sensitive.  
  
If you are grouping multiple search terms, this filter is inherited by all child groups. | `case:yes Hello World`  
class: |  | Search for a class name. | `class:MainClass`  
content: |  | Search only for file names and file contents. | `content:hello`  
file: | filepath:  
path:  
f: | Search for a file by its path. | `file:test.js`  
function: | func: | Search for a function name. | `function:print`  
lang: | language: | Search for results by using a specific language. | `lang:java test`  
  
### Search operators

The following table lists the operators you can use when searching code.

Operator | Other options | Description  
---|---|---  
AND |  | Logical `AND` operator. For more information, see Using the AND operator.  
OR |  | Logical `OR` operator. For more information, see Using the OR operator.  
([SEARCH_EXPRESSION]) |  | Groups multiple terms together. For more information, see  Grouping search terms.  
- |  | Excludes the term from search results.  
\ |  | Escapes special characters such as `.`, `\`, or `(`.  
"[SEARCH_EXPRESSION]" |  | Perform a search without interpreting the search query as a regular expression.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
