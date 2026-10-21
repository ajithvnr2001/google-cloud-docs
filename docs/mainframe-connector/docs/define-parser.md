---
url: https://docs.cloud.google.com/mainframe-connector/docs/define-parser/
title: Define the copybook parser \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:37:25.905187+00:00
---

# Define the copybook parser  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/define-parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Define the copybook parser Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Connector supports two versions of the copybook parser:

  * **Native copybook parser:** The Native copybook parser is the latest version of the parser. The Native copybook parser implements an ANTLR4 based parser and supports COBOL copybooks. For more information on the features supported by the Native copybook parser and the restrictions of its use, see [Native copybook parser](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#native-copybook-parser).
  * **Legacy copybook parser:** The legacy copybook parser is an older version of the parser that supports non-COBOL features. If you are using Domain-Specific Language (DSL) based-copybook the legacy parser might be more suitable as the Native copybook parser might cause errors. For more information on the features supported by the legacy copybook parser and the restrictions of its use, see [Legacy copybook parser](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#legacy-copybook-parser).

**Note:** The Legacy parser is being deprecated. We recommend that you switch to the Native copybook parser.



You can define which parser you want to use based on your copybook by using the `parser_type=legacy|copybook` flag. The default value is `auto` which is the auto-detect mode. The auto-detect mode prioritizes using the Native copybook parser, which is suitable for parsing COBOL-based copybooks. However, if you are using a non-COBOL-based copybook with the old format, the `parser_type=legacy` flag offers backward compatibility helping you use the Legacy copybook parser.

**Note:** You cannot explicitly set `parser_type` to `auto` from the command line.

The following table defines the behavior of Mainframe Connector based on the flag.

Flag | Action  
---|---  
`auto` | Mainframe Connector detects the parser automatically and executes three parsing attempts in the following order: 

  * Parses using the Native parser and the explicit comment area in columns 1-6. If parsing is successful, Mainframe Connector logs the parser that is used and returns the result. If parsing fails, Mainframe Connector tries the next parser.
  * Parses using the Native parser without the comment area. If parsing is successful, Mainframe Connector logs the parser that is used and returns the result. If parsing fails, Mainframe Connector tries the next parser.
  * Parses using the Legacy parser. If parsing is successful, Mainframe Connector logs the parser that is used and returns the result. If parsing fails, Mainframe Connector shows an error.

  
`legacy` | The Legacy parser is used for parsing. It expects a COBOL look-a-like copybook such as a Domain-Specific Language (DSL)-based copybook. When you use the `legacy` flag, Mainframe Connector shows a warning that the Legacy parser will get deprecated. After using the Legacy parser for parsing, Mainframe Connector compares the result of the Legacy parser with that of the Native parser by executing two parsing attempts in the following order: 

  * Parses the copybook using the Native parser expecting an explicit comment area in columns 1-6. If parsing is successful, Mainframe Connector compares the parsed result with that of the Legacy parser. If it is not equal, a warning is shown. If parsing fails, Mainframe Connector tries the next parser.
  * Parses the copybook using the Native parser without comment area in columns 1-6. If parsing is successful, Mainframe Connector compares the parsed result with that of the Legacy parser. If it is not equal a warning is shown. If parsing fails, Mainframe Connector logs the exception.

  
`copybook` | The Native copybook parser is used for parsing. It expects Native copybooks as input, including an explicit comment area in columns 1-6. If parsing fails Mainframe Connector shows an error.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
