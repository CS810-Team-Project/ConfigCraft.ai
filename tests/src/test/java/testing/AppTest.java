import org.junit.jupiter.api.Test;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

@Testcontainers
public class AppTest {

    @Container
    private final GenericContainer<?> javaContainer = new GenericContainer<>("openjdk:latest")
            .withFileSystemBind(".", "/usr/src/app");

    @Test
    void TestApp() {
        // Compile the Java file inside the Docker container
        String compileCommand = "javac outputFile.java";
        String compilationOutput = javaContainer.execInContainer("/bin/sh", "-c", compileCommand).getStdout();

        // Assert that there are no compilation errors
        // You might need to parse the compilation output to check for errors
        // Assertions.assertTrue(compilationOutput.contains("error"), "Compilation failed: " + compilationOutput);
    }
}