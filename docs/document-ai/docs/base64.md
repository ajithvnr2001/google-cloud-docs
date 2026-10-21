---
url: https://docs.cloud.google.com/document-ai/docs/base64/
title: Base64 encoding \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:17.369063+00:00
---

# Base64 encoding  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/base64/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Base64 encoding Stay organized with collections  Save and categorize content based on your preferences. 

When sending document files to the Document AI API, you can send data directly in the [`RawDocument.content`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/RawDocument) field with [online processing](https://docs.cloud.google.com/document-ai/docs/send-request#online-process) **only** if your file is [20 MB or less](https://docs.cloud.google.com/document-ai/quotas#content_limits). The input file will be in a binary format, which must be encoded before sending to Document AI.

If your input file exceeds the online processing limits, it must be stored in a Cloud Storage bucket in order to be sent for processing, which does not require encoding. Refer to the [batch processing documentation](https://docs.cloud.google.com/document-ai/docs/send-request#batch-process) for details.

## Using the command line

Within a gRPC request, you can simply write binary data out directly; however, JSON is used when making a REST request. JSON is a text format that does not directly support binary data, so you will need to convert such binary data into text using [Base64](https://en.wikipedia.org/wiki/Base64) encoding.

Most development environments contain a native `base64` utility to encode a binary into ASCII text data. To encode a file:

### Linux

Encode the file using the `base64` command line tool, making sure to prevent line-wrapping by using the `-w 0` flag:
    
    
    base64 INPUT_FILE -w 0 > OUTPUT_FILE
    

### macOS

Encode the file using the `base64` command line tool:
    
    
    base64 -i INPUT_FILE -o OUTPUT_FILE
    

### Windows

Encode the file using the `Base64.exe` tool:
    
    
    Base64.exe -e INPUT_FILE > OUTPUT_FILE
    

### PowerShell

Encode the file using the `Convert.ToBase64String` method:
    
    
    [Convert]::ToBase64String([IO.File]::ReadAllBytes("./INPUT_FILE")) > OUTPUT_FILE
    

Create a JSON request file, inlining the base64-encoded data:

### JSON
    
    
    {
      "skipHumanReview": skipHumanReview,
      "rawDocument": {
        "mimeType": "MIME_TYPE",
        "content": "BASE64_ENCODED_DATA"
      },
      "fieldMask": "FIELD_MASK"
    }

## Using client libraries

Embedding binary data into requests through text editors is neither desirable or practical. In practice, you will be embedding base64 encoded files within client code. All supported programming languages have built-in mechanisms for base64 encoding content.

### Python
    
    
    # Import the base64 encoding library.
    import base64
    
    # Pass the image data to an encoding function.
    def encode_image(image):
        with open(image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    

### Node.js
    
    
    // Read the file into memory.
    var fs = require('fs');
    var imageFile = fs.readFileSync('/path/to/file');
    
    // Convert the image data to a Buffer and base64 encode it.
    var encoded = Buffer.from(imageFile).toString('base64');
    

### Java
    
    
    // Import the Base64 encoding library.
    import org.apache.commons.codec.binary.Base64;
    
    // Encode the image.
    String encodedString = Base64.getEncoder().encodeToString(imageFile.getBytes());
    

### Go
    
    
    import (
        "bufio"
        "encoding/base64"
        "io"
        "os"
    )
    
    // Open image file.
    f, _ := os.Open("image.jpg")
    
    // Read entire image into byte slice.
    reader := bufio.NewReader(f)
    content, _ := io.ReadAll(reader)
    
    // Encode image as base64.
    base64.StdEncoding.EncodeToString(content)
    

[ Previous arrow_back  Evaluate performance  ](https://docs.cloud.google.com/document-ai/docs/evaluate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
