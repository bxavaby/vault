package com.example;

import org.apache.commons.io.FileUtils;
import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class TextProcessor {
    public static void main(String[] args) throws IOException {
        File inputDir = new File("input");
        File outputDir = new File("output");

        if (!inputDir.exists() || !outputDir.exists()) {
            System.out.println("Please run Gradle tasks first to setup directories and files!");
            return;
        }

        File inputFile = new File(inputDir, "sample.txt");
        String content = FileUtils.readFileToString(inputFile, StandardCharsets.UTF_8);
        System.out.println("Processing file: " + inputFile.getAbsolutePath());
        System.out.println("Content preview: " + content.substring(0, Math.min(content.length(), 50)) + "...");
    }
}
