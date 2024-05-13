package com.stevens;

import soot.*;
import soot.options.*;

public class Verifier1 {
    public void verify() {
        // Initialize the Soot framework
        G.v().out.println("Initializing Soot...");
        Options.v().set_output_format(Options.output_format_jimple);
        G.v().out.println("Soot initialized successfully!");

        // Set up necessary configurations
        G.v().out.println("Setting up configurations...");
        String jrePath = System.getProperty("java.home") + "/lib/rt.jar";
        // print the path to the rt.jar file
        G.v().out.println("Path to rt.jar: " + jrePath);
        Options.v().set_soot_classpath(jrePath + ":" + System.getProperty("java.class.path"));
        Options.v().set_whole_program(true);
        Options.v().set_allow_phantom_refs(true);
        G.v().out.println("Configurations set up successfully!");

        // Invoke Soot on the target class
        Scene.v().loadNecessaryClasses();
        G.v().out.println("Invoking Soot on the target class...");
        Scene.v().loadClassAndSupport("java.util.concurrent.ThreadPoolExecutor");
        G.v().out.println("Soot invoked successfully on the target class!");

        // Analyze the target class for common security vulnerabilities
        G.v().out.println("Analyzing the target class for common security vulnerabilities...");
        SootClass sootClass = Scene.v().getSootClass("java.util.concurrent.ThreadPoolExecutor");
        for (SootMethod m : sootClass.getMethods()) {
            G.v().out.println("Analyzing method " + m.getSignature() + "...");
            if (m.isConcrete()) {
                Body body = m.retrieveActiveBody();
                for (Unit u : body.getUnits()) {
                    // Print CFGs for each unit in the method
                    G.v().out.println(u);
                }
            }
        }
        G.v().out.println("Finished analyzing the target class!");
    }
}
