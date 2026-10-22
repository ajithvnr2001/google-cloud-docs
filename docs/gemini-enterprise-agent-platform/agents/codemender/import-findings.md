---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender/import-findings/
title: Import third-party security findings \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:03.742060+00:00
---

# Import third-party security findings  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender/import-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Import third-party security findings Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you already use third-party static analysis or vulnerability scanning tools, you can import findings directly into CodeMender to proceed immediately to verification and patching.

## Import security reports

CodeMender parses external security reports and registers findings in its local database.

### Import a JSON findings file

To import findings from a JSON file, use the `--file` (or `-f`) flag. The JSON file must conform to the following schema:
    
    
    [
      {
        "file_path": "src/auth/session_manager.py",
        "line": 42,
        "title": "SQL Injection",
        "message": "Raw user input concatenated in SQL query",
        "severity": "HIGH",
        "vuln_type": "CWE-89"
      }
    ]
    

Run the import command:
    
    
    cm report import --file ./findings.json
    

### Interactive import mode

If you don't have a JSON file, you can run the import command without the `--file` flag to enter an interactive wizard in your terminal:
    
    
    cm report import
    

Follow the prompts to enter the path, line number, severity, and description for each finding. Enter `q` at any prompt to finish and save.

## Process imported findings

After importing external findings:

  1. Run `cm report` to view the list of registered findings and obtain their generated `<finding-id>` values.
  2. Execute verification on an imported finding to generate a proof-of-concept exploit: 
         
         cm verify FINDING_ID

  3. Generate and validate a security patch for the finding: 
         
         cm fix FINDING_ID




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
