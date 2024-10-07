// Filename: MergedContributions_TimAnderson.pseudocode

start
    // Declarations
    string roomAName
    num roomAValue
    string roomBName
    num roomBValue
    string bothFilesDone = "N" // Indicates if both input files have been processed
    num HIGH_VALUE = 999999 // A high value to indicate end of file

    InputFile roomAFile
    InputFile roomBFile
    OutputFile mergedFile

    getReady() // Initialize file streams and read initial data

    // Continue until both files are processed
    while bothFilesDone = "N"
        detailLoop() // Process the records
    endwhile

    allDone() // Clean up and close files
stop

// Function to open files and read initial data
getReady()
    open roomAFile "roomAFile.dat"
    open roomBFile "roomBFile.dat"
    open mergedFile "mergedFile.dat"

    // Read initial values from both files
    readA()
    readB()
    checkBoth()
return

// Function to read data from Room A file
readA()
    input roomAName, roomAValue from roomAFile
    if eof then
        roomAValue = HIGH_VALUE // Set to HIGH_VALUE if end of file is reached
    endif
return

// Function to read data from Room B file
readB()
    input roomBName, roomBValue from roomBFile
    if eof then
        roomBValue = HIGH_VALUE // Set to HIGH_VALUE if end of file is reached
    endif
return

// Function to check if both files have been processed
checkBoth()
    if roomAValue = HIGH_VALUE AND roomBValue = HIGH_VALUE then
        bothFilesDone = "Y" // Set flag if both files are done
    endif
return

// Function to process records from both homerooms
detailLoop()
    if roomAValue > roomBValue then
        output roomBName, roomBValue to mergedFile // Output from Room B
        readB() // Read next value from Room B
    else
        output roomAName, roomAValue to mergedFile // Output from Room A
        readA() // Read next value from Room A
    endif
return

// Function to close all opened files
allDone()
    close roomAFile // Close Room A file
    close roomBFile // Close Room B file
    close mergedFile // Close the merged output file
return
