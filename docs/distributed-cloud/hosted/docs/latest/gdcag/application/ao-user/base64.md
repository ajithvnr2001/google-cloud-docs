---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/base64/
title: Vertex AI services \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:44.453364+00:00
---

# Vertex AI services  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/base64/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Vertex AI services Stay organized with collections  Save and categorize content based on your preferences. 

## Base64 encoding

You can provide image data for optical character recognition by specifying the URI path to the image, or by sending the image data as base64-encoded text.

Most development environments contain a native `base64` utility to encode a binary image into ASCII text data. To encode an image file:

### Linux
    
    
        base64 input.jpg > output.txt
    

### Mac OSX
    
    
        base64 -i input.jpg -o output.txt
    

### Windows
    
    
        C:> Base64.exe -e input.jpg > output.txt

### PowerShell
    
    
        [Convert]::ToBase64String([IO.File]::ReadAllBytes("./input.jpg")) > output.txt

You can then use this output image data natively within the JSON request:
    
    
    {
      "requests":[
        {
          "image":{
            "content": "BASE64_ENCODED_DATA"
          },
          "features": [
            {
              "type":"TEXT_DETECTION",
              "maxResults":1
            }
          ]
        }
      ]
    }
    

Each programming language has its own way of base64 encoding image files:

### Python

In Python, you can base64-encode image files as follows:
    
    
    # Import the base64 encoding library.
    import base64
    
    # Pass the image data to an encoding function.
    def encode_image(image):
      image_content = image.read()
      return base64.b64encode(image_content)
    

### Node.js

In Node.js, you can base64-encode image files as follows:
    
    
    // Read the file into memory.
    var fs = require('fs');
    var imageFile = fs.readFileSync('/path/to/file');
    
    // Convert the image data to a Buffer and base64 encode it.
    var encoded = Buffer.from(imageFile).toString('base64');
    

### Java

In Java, you can base64-encode image files as follows:
    
    
    // Import the Base64 encoding library.
    import org.apache.commons.codec.binary.Base64;
    
    // Encode the image.
    byte[] imageData = Base64.encodeBase64(imageFile.getBytes());
    

### Go

In Go, you can base64-encode image files as follows:
    
    
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
