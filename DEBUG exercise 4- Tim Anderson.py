start
    Declarations
        num mortgagePayment
        num utilities
        num taxes
        num upkeep
        num total
    
    startUp()  // Initialize the program by getting the first mortgage payment

    while mortgagePayment <> 0 do  // Loop until the user enters 0 for mortgage payment
        mainLoop()  // Calculate and display the total home ownership cost
    endwhile

    finishUp()  // End the program with a closing message
stop

// Start-up function to get the initial mortgage payment
startUp()
    output "Enter your mortgage payment or 0 to quit"
    input mortgagePayment  // Corrected from 'mtgPayment' to match the variable name
return

// Main loop function to compute the total cost
mainLoop()
    output "Enter utilities"
    input utilities

    output "Enter taxes"
    input taxes

    output "Enter amount for upkeep"
    input upkeep

    // Calculate the total cost of home ownership
    total = mortgagePayment + utilities + taxes + upkeep

    // Output the total cost
    output "Total is ", total
return

// Finish-up function to display the end of the program message
finishUp()
    output "End of program"
return
