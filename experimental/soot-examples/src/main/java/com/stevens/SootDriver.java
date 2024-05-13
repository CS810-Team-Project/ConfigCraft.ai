// package com.stevens;

// import java.util.concurrent.ThreadPoolExecutor;
// import soot.*;
// import soot.jimple.*;
// import soot.toolkits.graph.*;

// public class SootDriver {
//     public static void main(String[] args) {
//         // Initialize Soot
//         G.v().out.println("Initializing Soot...");
//         Scene scene = new Scene();
//         scene.addBasicClass("java.util.concurrent.ThreadPoolExecutor", SootClass.BODIES);

//         // Get the ThreadPoolExecutor class
//         SootClass threadPoolExecutorClass = scene.getSootClass("java.util.concurrent.ThreadPoolExecutor");

//         // Iterate over all methods in the class
//         for (SootMethod method : threadPoolExecutorClass.getMethods()) {
//             // Skip non-static methods
//             if (!method.isStatic()) continue;

//             // Get the body of the method
//             SootBody body = method.retrieveActiveBody();

//             // Create a new CFG for the method
//             ControlFlowGraph cfg = new ControlFlowGraph(body);

//             // Print the CFG to standard output
//             G.v().out.println("CFG for " + method.getName() + ":");
//             G.v().out.println(cfg);
//         }
//     }
// }