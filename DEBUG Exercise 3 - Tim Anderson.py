start
    Declarations
        string name
        string EOFNAME = "ZZZZ"  // Added quotation marks for the string

    // Loop to keep asking for employee names until EOFNAME is entered
    housekeeping()  // Initialize and prompt for the first name

    while name <> EOFNAME do
        mainLoop()  // Process net pay for each employee
    endwhile
    
    finish()  // End the program and display the final message
stop

// Housekeeping function to get the first name or quit
housekeeping()
    output "Enter first name or ", EOFNAME, " to quit "
    input name  // Capture employee name
return

// Main loop function to calculate net pay
mainLoop()
    Declarations
        num hours
        num rate
        num DEDUCTION = 45  // Deduction is a numeric value
        num gross
        num net

    // Prompt for hours worked and hourly rate
    output "Enter hours worked for ", name
    input hours
    output "Enter hourly rate for ", name
    input rate
    
    // Calculate gross pay and net pay after deduction
    gross = hours * rate
    net = gross - DEDUCTION
    
    // Check if the employee earns enough to cover the deduction
    if net > 0 then
        output "Net pay for ", name, " is ", net
    else
        output "Deductions not covered. Net is 0."
    endif
    
    // Prompt for the next employee's name or to quit
    output "Enter next name or ", EOFNAME, " to quit "
    input name
return

// Finish function to display the end of job message
finish()
    output "End of job"
return
