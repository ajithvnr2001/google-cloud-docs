---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-Runnable-Script/
title: Batch V1 API - Class Google::Cloud::Batch::V1::Runnable::Script (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:30.494431+00:00
---

# Batch V1 API - Class Google::Cloud::Batch::V1::Runnable::Script (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-Runnable-Script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Batch V1 API - Class Google::Cloud::Batch::V1::Runnable::Script (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.2  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.21.0  0.20.1  0.19.2  0.18.3  0.17.4  0.16.2  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.5  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.3  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Batch V1 API class Google::Cloud::Batch::V1::Runnable::Script.

Script runnable.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #path
    
    
    def path() -> ::String

**Returns**

  * (::String) — The path to a script file that is accessible from the host VM(s).

Unless the script file supports the default `#!/bin/sh` shell interpreter, you must specify an interpreter by including a [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix) as the first line of the file. For example, to execute the script using bash, include `#!/bin/bash` as the first line of the file. Alternatively, to execute the script using Python3, include `#!/usr/bin/env python3` as the first line of the file.

Note: The following fields are mutually exclusive: `path`, `text`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #path=
    
    
    def path=(value) -> ::String

**Parameter**

  * **value** (::String) — The path to a script file that is accessible from the host VM(s).

Unless the script file supports the default `#!/bin/sh` shell interpreter, you must specify an interpreter by including a [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix) as the first line of the file. For example, to execute the script using bash, include `#!/bin/bash` as the first line of the file. Alternatively, to execute the script using Python3, include `#!/usr/bin/env python3` as the first line of the file.

Note: The following fields are mutually exclusive: `path`, `text`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The path to a script file that is accessible from the host VM(s).

Unless the script file supports the default `#!/bin/sh` shell interpreter, you must specify an interpreter by including a [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix) as the first line of the file. For example, to execute the script using bash, include `#!/bin/bash` as the first line of the file. Alternatively, to execute the script using Python3, include `#!/usr/bin/env python3` as the first line of the file.

Note: The following fields are mutually exclusive: `path`, `text`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text
    
    
    def text() -> ::String

**Returns**

  * (::String) — The text for a script.

Unless the script text supports the default `#!/bin/sh` shell interpreter, you must specify an interpreter by including a [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix) at the beginning of the text. For example, to execute the script using bash, include `#!/bin/bash\n` at the beginning of the text. Alternatively, to execute the script using Python3, include `#!/usr/bin/env python3\n` at the beginning of the text.

Note: The following fields are mutually exclusive: `text`, `path`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text=
    
    
    def text=(value) -> ::String

**Parameter**

  * **value** (::String) — The text for a script.

Unless the script text supports the default `#!/bin/sh` shell interpreter, you must specify an interpreter by including a [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix) at the beginning of the text. For example, to execute the script using bash, include `#!/bin/bash\n` at the beginning of the text. Alternatively, to execute the script using Python3, include `#!/usr/bin/env python3\n` at the beginning of the text.

Note: The following fields are mutually exclusive: `text`, `path`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The text for a script.

Unless the script text supports the default `#!/bin/sh` shell interpreter, you must specify an interpreter by including a [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix) at the beginning of the text. For example, to execute the script using bash, include `#!/bin/bash\n` at the beginning of the text. Alternatively, to execute the script using Python3, include `#!/usr/bin/env python3\n` at the beginning of the text.

Note: The following fields are mutually exclusive: `text`, `path`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
