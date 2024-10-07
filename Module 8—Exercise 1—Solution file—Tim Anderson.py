BEGIN
    DECLARE InputFile geraldineFile
    DECLARE InputFile gerardFile
    DECLARE OutputFile mergedFile

    // Sample customer records for Geraldine's Landscaping Service
    DECLARE geraldineRecords AS List
    geraldineRecords = [
        (4891, "Smith", "South Bend", 1500),
        (4978, "Miller", "Bloomington", 9800),
        (5144, "Johnson", "Terre Haute", 3500)
    ]

    // Sample customer records for Gerard's Landscaping Service
    DECLARE gerardRecords AS List
    gerardRecords = [
        (8949, "Garcia", "Fort Wayne", 2500),
        (9841, "Brown", "Gary", 3000)
    ]

    OPEN mergedFile FOR WRITING "MergedBusinesses.csv"

    DECLARE uniqueCustomers AS List

    // Read records from Geraldine's landscaping service
    FOR EACH record IN geraldineRecords DO
        IF NOT EXISTS(record.customerNumber IN uniqueCustomers) THEN
            ADD record TO uniqueCustomers
        END IF
    END FOR

    // Read records from Gerard's landscaping service
    FOR EACH record IN gerardRecords DO
        IF NOT EXISTS(record.customerNumber IN uniqueCustomers) THEN
            ADD record TO uniqueCustomers
        END IF
    END FOR

    // Write unique records to merged file
    FOR EACH customer IN uniqueCustomers DO
        WRITE customer TO mergedFile
    END FOR

    CLOSE mergedFile
END
