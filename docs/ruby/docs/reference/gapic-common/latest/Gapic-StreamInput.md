---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput/
title: gapic-common - Class Gapic::StreamInput (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:16.418921+00:00
---

# gapic-common - Class Gapic::StreamInput (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::StreamInput (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::StreamInput.

Manages requests for an input stream and holds the stream open until [#close](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput#Gapic__StreamInput_close_instance_ "Gapic::StreamInput#close \(method\)") is called.

## Inherits

  * Object 



## Methods 

### #<<
    
    
    def <<(request) -> StreamInput

**Alias Of** : [#push](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput#Gapic__StreamInput_push_instance_)

Adds a request object to the stream.

**Parameter**

  * **request** (Object) 



**Returns**

  * ([StreamInput](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput)) — Returns self. 



### #append
    
    
    def append(request) -> StreamInput

**Alias Of** : [#push](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput#Gapic__StreamInput_push_instance_)

Adds a request object to the stream.

**Parameter**

  * **request** (Object) 



**Returns**

  * ([StreamInput](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput)) — Returns self. 



### #close
    
    
    def close() -> StreamInput

Closes the stream.

**Returns**

  * ([StreamInput](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput)) — Returns self. 



### #initialize
    
    
    def initialize(*requests) -> StreamInput

Create a new input stream object to manage streaming requests and hold the stream open until [#close](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput#Gapic__StreamInput_close_instance_ "Gapic::StreamInput#close \(method\)") is called.

**Parameter**

  * **requests** (Object) 



**Returns**

  * ([StreamInput](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput)) — a new instance of StreamInput 



### #push
    
    
    def push(request) -> StreamInput

**Aliases**

  * [#<<](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput#Gapic__StreamInput_<<_instance_)
  * [#append](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput#Gapic__StreamInput_append_instance_)



Adds a request object to the stream.

**Parameter**

  * **request** (Object) 



**Returns**

  * ([StreamInput](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-StreamInput)) — Returns self. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
