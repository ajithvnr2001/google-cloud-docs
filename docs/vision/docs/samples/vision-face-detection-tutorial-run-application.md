---
url: https://docs.cloud.google.com/vision/docs/samples/vision-face-detection-tutorial-run-application/
title: Running the app for face detection \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:24.250816+00:00
---

# Running the app for face detection  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-face-detection-tutorial-run-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Running the app for face detection Stay organized with collections  Save and categorize content based on your preferences. 

Run the app that draws boxes around detected faces in an image.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Face detection tutorial](https://docs.cloud.google.com/vision/docs/face-tutorial)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Annotates an image using the Vision API. */
    public static void main(String[] args) throws IOException, GeneralSecurityException {
      if (args.length != 2) {
        System.err.println("Usage:");
        System.err.printf(
            "\tjava %s inputImagePath outputImagePath\n", FaceDetectApp.class.getCanonicalName());
        System.exit(1);
      }
      Path inputPath = Paths.get(args[0]);
      Path outputPath = Paths.get(args[1]);
      if (!outputPath.toString().toLowerCase().endsWith(".jpg")) {
        System.err.println("outputImagePath must have the file extension 'jpg'.");
        System.exit(1);
      }
    
      FaceDetectApp app = new FaceDetectApp(getVisionService());
      List<FaceAnnotation> faces = app.detectFaces(inputPath, MAX_RESULTS);
      System.out.printf("Found %d face%s\n", faces.size(), faces.size() == 1 ? "" : "s");
      System.out.printf("Writing to file %s\n", outputPath);
      app.writeWithFaces(inputPath, outputPath, faces);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function main(inputFile, outputFile) {
      const PImage = require('pureimage');
      outputFile = outputFile || 'out.png';
      const faces = await detectFaces(inputFile);
      console.log('Highlighting...');
      await highlightFaces(inputFile, faces, outputFile, PImage);
      console.log('Finished!');
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    call_user_func($imageWriteFunc[$ext], $outputImage, $outFile);
    printf('Output image written to %s' . PHP_EOL, $outFile);

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def main(input_filename, output_filename, max_results):
        with open(input_filename, "rb") as image:
            faces = detect_face(image, max_results)
            print("Found {} face{}".format(len(faces), "" if len(faces) == 1 else "s"))
    
            print(f"Writing to file {output_filename}")
            # Reset the file pointer, so we can read the file again
            image.seek(0)
            highlight_faces(image, faces, output_filename)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
