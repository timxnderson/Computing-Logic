START

FUNCTION calculateBill(textMessages):
    BASE_FEE = 5
    TAX_RATE = 0.14
    ADDITIONAL_FEE_100_TO_300 = 0.03
    ADDITIONAL_FEE_ABOVE_300 = 0.02

    IF textMessages <= 100 THEN
        totalBill = BASE_FEE
    ELSE IF textMessages <= 300 THEN
        totalBill = BASE_FEE + (textMessages - 100) * ADDITIONAL_FEE_100_TO_300
    ELSE
        totalBill = BASE_FEE + (200 * ADDITIONAL_FEE_100_TO_300) + (textMessages - 300) * ADDITIONAL_FEE_ABOVE_300
    
    totalWithTax = totalBill * (1 + TAX_RATE)
    RETURN totalBill, totalWithTax

MAIN
    DECLARE areaCode, phoneNumber, textMessages
    DECLARE customerData AS LIST OF TUPLES (areaCode, phoneNumber, textMessages, totalBill, totalWithTax)
    
    WHILE TRUE DO
        INPUT "Enter area code (or type 'exit' to finish): " INTO areaCode
        IF areaCode == 'exit' THEN
            BREAK
        
        INPUT "Enter phone number: " INTO phoneNumber
        INPUT "Enter total number of text messages sent: " INTO textMessages
        
        totalBill, totalWithTax = calculateBill(textMessages)

        DISPLAY "Area Code: ", areaCode
        DISPLAY "Phone Number: ", phoneNumber
        DISPLAY "Total Text Messages: ", textMessages
        DISPLAY "Monthly Bill Before Tax: ", totalBill
        DISPLAY "Monthly Bill After Tax: ", totalWithTax

        ADD (areaCode, phoneNumber, textMessages, totalBill, totalWithTax) TO customerData

    // Scenario 2: Display customers who sent over 100 messages
    DISPLAY "Customers who sent over 100 messages:"
    FOR EACH customer IN customerData DO
        IF customer[2] > 100 THEN
            DISPLAY customer

    // Scenario 3: Display customers with bills exceeding $10
    DISPLAY "Customers with total bill exceeding $10:"
    FOR EACH customer IN customerData DO
        IF customer[4] > 10 THEN
            DISPLAY customer

    // Scenario 4: Prompt for area code and display related bills
    INPUT "Enter area code to view bills from that area: " INTO targetAreaCode
    DISPLAY "Bills from area code: ", targetAreaCode
    FOR EACH customer IN customerData DO
        IF customer[0] == targetAreaCode THEN
            DISPLAY customer

END
