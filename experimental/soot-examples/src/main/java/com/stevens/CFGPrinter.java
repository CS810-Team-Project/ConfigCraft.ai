package com.stevens;
import soot.*;
import soot.options.Options;
import soot.toolkits.graph.ExceptionalUnitGraph;
import soot.toolkits.graph.UnitGraph;

public class CFGPrinter {
    public void printCFG() {
        // Initialize Soot with the necessary configurations
        soot.G.reset();

        // Adding the Java library classpath to Soot
        String classpath = Scene.v().getSootClassPath() + System.getProperty("path.separator") + System.getProperty("java.home") + "/lib/rt.jar";
        Scene.v().setSootClassPath(classpath);

        // Set up configuration to use Jimple as the intermediate representation
        Options.v().set_output_format(Options.output_format_jimple);
        Options.v().set_src_prec(Options.src_prec_java);
        Options.v().set_whole_program(true);
        Options.v().set_allow_phantom_refs(true);

        // Load the ThreadPoolExecutor class
        Scene.v().addBasicClass("java.util.concurrent.ThreadPoolExecutor", SootClass.HIERARCHY);
        Scene.v().loadNecessaryClasses();
        SootClass sootClass = Scene.v().getSootClass("java.util.concurrent.ThreadPoolExecutor");

        // Ensuring that all methods have active bodies
        for (SootMethod method : sootClass.getMethods()) {
            if (!method.isConcrete()) continue;
            method.retrieveActiveBody();
        }

        // Print CFGs for each concrete method
        for (SootMethod method : sootClass.getMethods()) {
            if (!method.isConcrete()) continue;
            System.out.println("Method: " + method.getSignature());
            Body body = method.retrieveActiveBody();
            UnitGraph cfg = new ExceptionalUnitGraph(body);

            // Printing the basic blocks of the CFG
            cfg.iterator().forEachRemaining(unit -> {
                System.out.println(unit.toString());
                cfg.getSuccsOf(unit).forEach(successor -> System.out.println("  --> " + successor.toString()));
            });
            System.out.println("=================================");
        }
    }
}