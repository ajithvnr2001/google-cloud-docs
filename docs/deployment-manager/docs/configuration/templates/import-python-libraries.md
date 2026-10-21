---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/import-python-libraries/
title: Importing Python Libraries \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:55.165089+00:00
---

# Importing Python Libraries  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/import-python-libraries/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Importing Python Libraries Stay organized with collections  Save and categorize content based on your preferences. 

You can use Python libraries in your Python templates. Deployment Manager uploads and runs the Python code in your templates in a secure environment.

You can use libraries that are supported by Deployment Manager, listed below. To use a different Python library, import the full library source in your template.

## Supported libraries

Deployment Manager supports specific Python libraries that you can use in your templates. These libraries include:

  * [`base64`](https://docs.python.org/3/library/base64.html)
  * [`collections`](https://docs.python.org/3/library/collections.html)
  * [`encodings`](https://docs.python.org/3/library/codecs.html)
  * [`encodings.utf_8`](https://docs.python.org/3/library/codecs.html)
  * [`encodings.utf_16`](https://docs.python.org/3/library/codecs.html)
  * [`hashlib`](https://docs.python.org/3/library/hashlib.html)
  * [`json`](https://docs.python.org/3/library/json.html)
  * [`math`](https://docs.python.org/3/library/math.html)
  * [`random`](https://docs.python.org/3/library/random.html)
  * [`io`](https://docs.python.org/3/library/io.html)
  * [`sys`](https://docs.python.org/3/library/sys.html)
  * [`string`](https://docs.python.org/3/library/string.html)
  * [`time`](https://docs.python.org/3/library/time.html)
  * [`yaml`](https://github.com/yaml/pyyaml)
  * [`zipfile`](https://docs.python.org/3/library/zipfile.html)

**Caution:** Do not use system calls in your template. If a template contains any code that makes system or network calls, it is rejected. This includes any method that performs system calls using the supported libraries listed above. For example, `sys` contains a number of system calls that will automatically be rejected if you use them in your template.

If you want to import libraries that are not explicitly supported, import the library using the filename. This is especially useful if you want to import your own helper methods. The same restrictions for system calls apply to custom libraries as well.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
