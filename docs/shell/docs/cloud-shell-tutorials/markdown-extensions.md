---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/markdown-extensions/
title: Markdown extensions \u00a0|\u00a0 Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:24.277930+00:00
---

# Markdown extensions  |  Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/markdown-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Reference ](https://docs.cloud.google.com/shell/docs/apis)



Send feedback 

#  Markdown extensions Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Shell tutorials support Markdown extensions to expand the capability of the language.

## Code block formatting

To create a code block in your tutorial, use backticks:
    
    
    ```
    print("hello world")
    ```
    

Code blocks support syntax highlighting and have a button to copy the code to the clipboard.

You can change the way a code block is displayed by adding a class name after the first set of backticks. For example, to tell a code block to syntax highlight as Python, you can add `py` as a class:
    
    
    **```py**
    print("hello world")
    ```
    

Here are some other classes you can use to change how a code block is shown:

Class | Effect  
---|---  
LANGUAGE_CLASS_NAME | Change the syntax highlighting to a specified supported language.  
`none` | Don't apply syntax highlighting to the code block.  
`sh` | Format the code like terminal input. The code is prefixed by a `$`, and a button is shown on the block that copies the code to Cloud Shell when clicked.  
`terminal` | Format the code like terminal output. Identical to the `none` style, except it has no copy buttons on the code block.  
  
Here are the supported language styles for syntax highlighting:

Language name | Class name  
---|---  
C# | `cs`  
C variants | `c`, `cc`, `cpp`, `cxx`, `cyc`, `m`  
Clojure | `clj`  
Coffeescript | `coffee`  
Command line | `bsh`, `csh`, `sh`  
CSS | `css`  
Go | `go`  
Haskell | `hs`  
Java | `java`  
Javascript | `js`  
JSON | `json`  
Kotlin | `kotlin`  
Lisp | `lisp`  
Lua | `lua`  
Markup  | `default-markup`, `htm`, `html`, `mxml`, `xml`, `xsl`  
OCaml, SML, F#, and similar languages | `fs`, `ml`  
Perl | `perl`, `pl`, `pm`  
Protocol buffers | `proto`  
Python | `cv`, `py`  
Ruby | `rb`  
Scala | `scala`  
SQL | `sql`  
Swift | `swift`  
VHDL '93 | `vhdl`  
Visual Basic | `vb`, `vbs`  
Wiki | `wiki`  
YAML | `yaml`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
