/*
 * Copyright (C) 2004-2021 Intel Corporation.
 * SPDX-License-Identifier: MIT
 */

//
// This tool counts the number of times a routine is executed and
// the number of instructions executed in a routine
//

#include <fstream>
#include <iomanip>
#include <iostream>
#include <string.h>
#include "pin.H"
using std::cerr;
using std::dec;
using std::endl;
using std::hex;
using std::ofstream;
using std::setw;
using std::string;
using std::cout;


// This function is called before every instruction is executed
VOID printreturn(ADDRINT x ) { 
    cout<<"return value = "<<x<<endl;
}

VOID printarg(ADDRINT x , ADDRINT *y ) { 
    cout<<"arg1 = "<<x<<" arg2 = "<<*y<<endl;
}

// Pin calls this function every time a new rtn is executed
VOID Routine(RTN rtn, VOID* v)
{
    // Allocate a counter for this routine

    // The RTN goes away when the image is unloaded, so save it now
    // because we need it in the fini
    string name     = RTN_Name(rtn);
    RTN_Open(rtn);
    if(name=="_Z3addic"){
    // Insert a call at the entry point of a routine to increment the call count
        RTN_InsertCall(rtn, IPOINT_AFTER, (AFUNPTR)printreturn, IARG_FUNCRET_EXITPOINT_VALUE , IARG_END);
        RTN_InsertCall(rtn, IPOINT_BEFORE, (AFUNPTR)printarg, IARG_FUNCARG_ENTRYPOINT_VALUE ,0, IARG_FUNCARG_ENTRYPOINT_REFERENCE ,1  , IARG_END);

    }
    RTN_Close(rtn);
    // For each instruction of the routine
}

// This function is called when the application exits
// It prints the name and count for each procedure
VOID Fini(INT32 code, VOID* v)
{

}

/* ===================================================================== */
/* Print Help Message                                                    */
/* ===================================================================== */

INT32 Usage()
{
    cerr << "This Pintool counts the number of times a routine is executed" << endl;
    cerr << "and the number of instructions executed in a routine" << endl;
    cerr << endl << KNOB_BASE::StringKnobSummary() << endl;
    return -1;
}

/* ===================================================================== */
/* Main                                                                  */
/* ===================================================================== */

int main(int argc, char* argv[])
{
    // Initialize symbol table code, needed for rtn instrumentation
    PIN_InitSymbols();


    // Initialize pin
    if (PIN_Init(argc, argv)) return Usage();

    // Register Routine to be called to instrument rtn
    RTN_AddInstrumentFunction(Routine, 0);

    // Register Fini to be called when the application exits
    PIN_AddFiniFunction(Fini, 0);

    // Start the program, never returns
    PIN_StartProgram();

    return 0;
}
