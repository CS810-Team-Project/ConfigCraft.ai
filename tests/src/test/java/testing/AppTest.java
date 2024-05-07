package testing;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.GenericContainer;

@Testcontainers
public class AppTest {

    @SuppressWarnings("deprecation")
    @Container
    private final GenericContainer<?> javaContainer = new GenericContainer<>("openjdk:latest")
            .withFileSystemBind(".", "/usr/src/app");

    @Test
    void TestApp() {
        // Compile the Java file inside the Docker container
        String compileCommand = "javac outputFile.java";
        String compilationOutput = "";

        try {
            compilationOutput = javaContainer.execInContainer("/bin/sh", "-c", compileCommand).getStdout();
        } catch(Exception e) {
            System.err.println("Failure when compiling");
        }
        // Assert that there are no compilation errors
        // You might need to parse the compilation output to check for errors
        Assertions.assertFalse(compilationOutput.contains("error"), "Compilation failed: " + compilationOutput);
    }
}