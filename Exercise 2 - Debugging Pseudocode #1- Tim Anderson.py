// Filename: MergedSalesData_TimAnderson.pseudocode

start
    // Declarations
    string newSalesperson
    num newAmount
    string usedSalesperson
    num usedAmount
    string bothAtEof = "N" // Indicates if both files have been processed
    string HIGH_NAME = "ZZZZZ" // A high value to indicate end of file

    InputFile newSales
    InputFile usedSales
    OutputFile allSales

    getReady() // Initialize file streams and read initial data

    // Continue until both files are processed
    while bothAtEof = "N"
        detailLoop() // Process the records
    endwhile

    finish() // Clean up and close files
stop

// Function to open files and read initial data
getReady()
    open newSales "NewSales.dat"
    open usedSales "UsedSales.dat"
    
    // Read initial records from both files
    input newSalesperson, newAmount from newSales
    if eof then
        newSalesperson = HIGH_NAME // If new sales file is empty, set newSalesperson to HIGH_NAME
    endif

    input usedSalesperson, usedAmount from usedSales
    if eof then
        usedSalesperson = HIGH_NAME // If used sales file is empty, set usedSalesperson to HIGH_NAME
    endif

    // Check if both files are empty
    if newSalesperson = HIGH_NAME AND usedSalesperson = HIGH_NAME then
        bothAtEof = "Y" // Set EOF flag if both files are empty
    endif
return

// Function to process records from both sales files
detailLoop()
    // Compare salesperson names and output the records in order
    if newSalesperson > usedSalesperson then 
        output usedSalesperson, usedAmount to allSales // Write the used sale
        input usedSalesperson, usedAmount from usedSales // Read next used sale
        if eof then
            usedSalesperson = HIGH_NAME // Handle EOF for used sales
        endif
    else 
        output newSalesperson, newAmount to allSales // Write the new sale
        input newSalesperson, newAmount from newSales // Read next new sale
        if eof then
            newSalesperson = HIGH_NAME // Handle EOF for new sales
        endif
    endif

    // Check if both sales records have been exhausted
    if newSalesperson = HIGH_NAME AND usedSalesperson = HIGH_NAME then
        bothAtEof = "Y" // Set EOF flag if both files are empty
    endif
return

// Function to close all opened files
finish()
    close newSales // Close the new sales file
    close usedSales // Close the used sales file
    close allSales // Close the output file
return
